#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import paramiko
import time

serverlist = ["106.10.42.67", "106.10.42.44", "106.10.42.151", "106.10.42.158", "106.10.42.161"]

data = json.loads(sys.argv[1])

# 입력받은 개수 만큼 서버 할당
for i in range(0, len(data)) :
    data[i]["ip"] = ''+serverlist[i]+''

master_id = []
master_ip = []
dual_id = []
dual_ip = []
slave_id = []
slave_ip = []

# 복제 환경 분류
for i in range(0, len(data)) :
    if data[i].get("master") == "null" :
        master_id.append(data[i]["id"])
        master_ip.append(data[i]["ip"])

    elif "slave" in data[i] :
        dual_id.append(data[i]["id"])
        dual_ip.append(data[i]["ip"])

    else :
        slave_id.append(data[i]["id"])
        slave_ip.append(data[i]["ip"])

print(data)

# master의 my.cnf 파일 수정, repl 계정 생성
for i in range(0, len(master_ip)) :

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
            client.connect('' +master_ip[i]+ '', 22, 'root')
    except:
            print("서버에 접속할 수 없습니다")
            sys.exit()

    cmd_list_master = ['echo server-id = '+master_id[i]+' >> /etc/my.cnf', 'echo log-bin = mysql-bin >> /etc/my.cnf', 'mysql -e \"Grant replication slave on *.* to \'repl\'@\'%\' identified by \'Ahstmxj@4\'\"', 'systemctl restart mysqld']
    req_master = ';'.join(cmd_list_master)
    client.exec_command(req_master)
    time.sleep(3)

# slave의 my.cnf 파일 수정, repl 계정 생성
for i in range(0, len(slave_ip)) :

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
            client.connect('' +slave_ip[i]+ '', 22, 'root')
    except:
            print("서버에 접속할 수 없습니다")
            sys.exit()

    cmd_list_slave = ['echo server-id = '+slave_id[i]+' >> /etc/my.cnf','mysql -e \"Grant replication slave on *.* to \'repl\'@\'%\' identified by \'Ahstmxj@4\'\"', 'systemctl restart mysqld']
    req_slave = ';'.join(cmd_list_slave)
    client.exec_command(req_slave)
    time.sleep(3)

for i in range(0, len(dual_ip)) :

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
            client.connect('' +dual_ip[i]+ '', 22, 'root')
    except:
            print("서버에 접속할 수 없습니다")
            sys.exit()

    cmd_list_dual = ['echo server-id = '+dual_id[i]+' >> /etc/my.cnf', 'echo log-bin = mysql-bin >> /etc/my.cnf', 'echo log-slave-updates >> /etc/my.cnf','mysql -e \"Grant replication slave on *.* to \'repl\'@\'%\' identified by \'Ahstmxj@4\'\"', 'systemctl restart mysqld']
    req_dual = ';'.join(cmd_list_dual)
    client.exec_command(req_dual)
    time.sleep(3)

time.sleep(3)

# master DB에서 binlog 값과  position 알아내기

for i in range(0, len(data)) :
     if data[i].get("master") == 'null' or 'slave' in data[i] :

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

# slave command 설정

for i in range(0, len(data)) :
    if data[i].get("master") is not "null" :
        target = data[i]["master"]
        for k in range(0, len(data)) :
            if data[k]["id"] == target :
                filename = data[k]["file"]
                pos = data[k]["pos"]
                ip = data[k]["ip"]

                try:
                    client.connect('' + data[i]["ip"] + '', 22, 'root')
                except:
                    print("서버에 접속할 수 없습니다")
                    sys.exit()

                cmd_list_master = ['mysql -e \"change master to ', 'master_host = \'' +ip+ '\',', 'master_port = 3306,', 'master_user = \'repl\',',
                                   'master_password =\'Ahstmxj@4\',', 'master_log_file= \'' +filename+ '\',', 'master_log_pos = ' +pos+ '\"']
                req_master = ''.join(cmd_list_master)
                stdin, stdout, stderr = client.exec_command(req_master)


# slave start
for i in range(0, len(data)) :
    if data[i].get("master") is not "null" :

                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                try:
                    client.connect('' + data[i]["ip"] + '', 22, 'root')
                except:
                    print("서버에 접속할 수 없습니다")
                    sys.exit()

                cmd_list_master = ['mysql -e \"start slave\"']
                req_master = ''.join(cmd_list_master)
                stdin, stdout, stderr = client.exec_command(req_master)
