#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import paramiko
import time
import pymysql

serverlist = ["106.10.42.44", "106.10.42.67", "106.10.42.151", "106.10.42.158", "106.10.42.161"]

data = json.loads(sys.argv[1])
repl = json.loads(sys.argv[2])

result_master = []
result_slave = []

# 입력받은 개수 만큼 서버 할당
for i in range(0, len(data)) :
    data[i]["ip"] = ''+serverlist[i]+''

# repl 계정 생성
def set_repl(id, pw):
    for i in range(0, len(data)) :

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        try:
            client.connect(''+data[i]["ip"]+'', 22, 'root')
        except:
                print("서버에 접속할 수 없습니다")
                sys.exit(1)


        client.exec_command('mysql -e \"Grant replication slave on *.* to \''+id+'\'@\'%\' identified by \''+pw+'\'\"')

# master, dual, slave의 my.cnf 파일 수정
def set_mycnf(data) :
    for i in range(0, len(data)) :

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
                client.connect('' +data[i]["ip"]+ '', 22, 'root')
        except:
                print("서버에 접속할 수 없습니다")
                sys.exit(1)

        if (data[i]["master"]=="Null") :
            cmd_list_master = ['echo server-id = '+data[i]["id"]+' >> /etc/my.cnf', 'echo log-bin = mysql-bin >> /etc/my.cnf']
            req_master = ';'.join(cmd_list_master)
            client.exec_command(req_master)
            client.exec_command('systemctl restart mysqld')
            client.close()

        elif('slave' in data[i]) :
            cmd_list_dual = ['echo server-id = '+data[i]["id"]+' >> /etc/my.cnf', 'echo log-bin = mysql-bin >> /etc/my.cnf', 'echo log-slave-updates >> /etc/my.cnf', 'echo report-host = nbp00' +data[i]["id"]+ ' >> /etc/my.cnf']
            req_dual = ';'.join(cmd_list_dual)
            client.exec_command(req_dual)
            client.exec_command('systemctl restart mysqld')
            client.close()

        else :
            cmd_list_slave = ['echo server-id = '+data[i]["id"]+' >> /etc/my.cnf', 'echo report-host = nbp00' +data[i]["id"]+ ' >> /etc/my.cnf']
            req_slave = ';'.join(cmd_list_slave)
            client.exec_command(req_slave)
            client.exec_command('systemctl restart mysqld')
            client.close()

# master DB에서 binlog 값과  position 알아내기
def get_masterinfo(data) :
    for i in range(0, len(data)) :
         if data[i].get("master") == 'Null' or 'slave' in data[i] :

             client = paramiko.SSHClient()
             client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

             try:
                 client.connect('' + data[i]["ip"] + '', 22, 'root')
             except:
                 print("서버에 접속할 수 없습니다")
                 sys.exit(1)

             cmd_list_master = ['mysql -e \"show master status\"']
             req_master = ''.join(cmd_list_master)
             stdin, stdout, stderr = client.exec_command(req_master)

             output = stdout.read()
             print(output)
             result1 = output.decode('ascii')
             result2 = str(result1)
             parser = result2.replace('\n', '\t')
             list = parser.split('\t')

             data[i]["file"]=''+list[5]+''
             data[i]["pos"]=''+list[6]+''
             client.close()

    return(data)

def set_slave(result) :
    for i in range(0, len(result)) :
        if result[i].get("master") is not "Null" :
            target = result[i]["master"]
            for k in range(0, len(data)) :
                if result[k]["id"] == target :
                    filename = result[k]["file"]
                    pos = result[k]["pos"]
                    ip = result[k]["ip"]

                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

                    try:
                        client.connect('' + result[i]["ip"] + '', 22, 'root')
                    except:
                        print("서버에 접속할 수 없습니다")
                        sys.exit(1)

                    cmd_list_master = ['mysql -e \"change master to ', 'master_host = \'' +ip+ '\',', 'master_port = 3306,', 'master_user = \'' +repl["id"]+ '\',',
                                       'master_password = \'' +repl["pw"]+ '\',', 'master_log_file= \'' +filename+ '\',', 'master_log_pos = ' +pos+ '\"']
                    req_master = ''.join(cmd_list_master)
                    stdin, stdout, stderr = client.exec_command(req_master)
                    client.close()

# slave start
def start_slave(result) :
    for i in range(0, len(result)) :
        if data[i].get("master") is not "Null" :

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                client.connect('' + result[i]["ip"] + '', 22, 'root')
            except:
                print("서버에 접속할 수 없습니다")
                sys.exit(1)

            client.exec_command('rm -rf /var/lib/mysql/auto.cnf')
            client.exec_command('systemctl restart mysqld')
            cmd_list_master = ['mysql -e \"start slave\"']
            req_master = ''.join(cmd_list_master)
            stdin, stdout, stderr = client.exec_command(req_master)

            client.close()

def result_replication(data) :

    for i in range(0, len(data)):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


        try:
            client.connect('' + data[i]["ip"] + '', 22, 'root')
        except:
            print("서버에 접속할 수 없습니다")
            sys.exit(1)


        if (data[i]["master"] == "Null") :

            cmd_list_showslavehosts = ['mysql -e \"show slave hosts\"']
            req_showslavehosts = ''.join(cmd_list_showslavehosts)
            stdin, stdout, stderr = client.exec_command(req_showslavehosts)
            output = stdout.read()
            output = ((output.decode('ascii')).replace('\n', '\t')).split('\t')
            k = int(len(output)/5)

            if (len(output) == 1 ) :
                result_master.append({"Master_id": "" + data[i]["id"] + "", "Error": "복제 과정 중 오류가 발생했습니다"})
            else :
                for i in range(1, k) :
                    result_master.append(dict(zip(output[:5:1], output[5*i:5*(i+1):1])))

        elif ("slave" in data[i]) :

            cmd_list_showslavehosts = ['mysql -e \"show slave hosts\"']
            req_showslavehosts = ''.join(cmd_list_showslavehosts)
            stdin, stdout, stderr = client.exec_command(req_showslavehosts)
            output = stdout.read()
            output = ((output.decode('utf-8')).replace('\n', '\t')).split('\t')
            k = int(len(output) / 5)

            if (len(output) == 1 ) :
                result_master.append({"Master_id": "" + data[i]["id"] + "", "Error": "복제 과정 중 오류가 발생했습니다"})
            else :
                for t in range(1, k) :
                    result_master.append(dict(zip(output[:5:1], output[5*t:5*(t+1):1])))

            cmd_list_showslavestatus = ['mysql -e \"show slave status\"']
            req_showslavestatus = ''.join(cmd_list_showslavestatus)
            stdin, stdout, stderr = client.exec_command(req_showslavestatus)
            output = stdout.read()
            output = ((output.decode('utf-8')).replace('\n', '\t')).split('\t')

            if (len(output) == 1):
                result_slave.append({"Slave_id":""+data[i]["id"]+"","Error":"복제 과정 중 오류가 발생했습니다"})
            else:
                result_slave.append({"Slave_id":""+data[i]["id"]+"","Slave_IO_Running":""+output[67]+"", "Slave_SQL_Running":""+output[68]+"", "Seconds_Behind_Master":""+output[89]})

        else :

            cmd_list_showslavestatus = ['mysql -e \"show slave status\"']
            req_showslavestatus = ''.join(cmd_list_showslavestatus)
            stdin, stdout, stderr = client.exec_command(req_showslavestatus)
            output = stdout.read()
            output = ((output.decode('utf-8')).replace('\n', '\t')).split('\t')

            if (len(output) == 1):
                result_slave.append({"Slave_id":""+data[i]["id"]+"","Error":"복제 과정 중 오류가 발생했습니다"})
            else:
                result_slave.append({"Slave_id":""+data[i]["id"]+"","Slave_IO_Running":""+output[67]+"", "Slave_SQL_Running":""+output[68]+"", "Seconds_Behind_Master":""+output[89]})

    client.close()
    return(result_master, result_slave)


def mysql_save(result_master, result_slave) :

    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='tnsdud24', db='test', charset='utf8')
    curs = db.cursor(pymysql.cursors.DictCursor)
    for i in range(0, len(result_master)) :
        mr = str(result_master[i]).replace('\'','\"')
        sql = "insert into master values (\'"+mr+"\')"
        curs.execute(sql)
        db.commit()

    for i in range(0, len(result_slave)) :
        sr = str(result_slave[i]).replace('\'', '\"')
        sql = "insert into slave values (\'" + sr + "\')"
        curs.execute(sql)
        db.commit()

    db.close()

set_repl(repl["id"],repl["pw"])

set_mycnf(data)

time.sleep(4)

result = get_masterinfo(data)

set_slave(result)

start_slave(result)

time.sleep(15)

result_replication(data)

mysql_save(result_master, result_slave)
