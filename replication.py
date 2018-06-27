#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import paramiko
import time

serverlist = ["106.10.42.44", "106.10.42.67", "106.10.42.151", "106.10.42.158", "106.10.42.161"]

data = json.loads(sys.argv[1])
repl = json.loads(sys.argv[2])

print(data)
print(repl)

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
                sys.exit()

        if (data[i]["master"]=="Null") :
            cmd_list_master = ['echo server-id = '+data[i]["id"]+' >> /etc/my.cnf', 'echo log-bin = mysql-bin >> /etc/my.cnf']
            req_master = ';'.join(cmd_list_master)
            client.exec_command(req_master)
            client.exec_command('systemctl restart mysqld')
            client.close()

        elif('slave' in data[i]) :
            cmd_list_dual = ['echo server-id = '+data[i]["id"]+' >> /etc/my.cnf', 'echo log-bin = mysql-bin >> /etc/my.cnf', 'echo log-slave-updates >> /etc/my.cnf']
            req_dual = ';'.join(cmd_list_dual)
            client.exec_command(req_dual)
            client.exec_command('systemctl restart mysqld')
            client.close()

        else :
            cmd_list_slave = ['echo server-id = '+data[i]["id"]+' >> /etc/my.cnf']
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
                 sys.exit()

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
                        sys.exit()

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
                sys.exit()

            client.exec_command('rm -rf /var/lib/mysql/auto.cnf')
            client.exec_command('systemctl restart mysqld')
            cmd_list_master = ['mysql -e \"start slave\"']
            req_master = ''.join(cmd_list_master)
            stdin, stdout, stderr = client.exec_command(req_master)

            client.close()

set_repl(repl["id"],repl["pw"])

set_mycnf(data)

time.sleep(4)

result = get_masterinfo(data)

print(result)

set_slave(result)

start_slave(result)
