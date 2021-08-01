import time
import hashlib
import termcolor
from urllib.request import urlopen

sha1hash = input(termcolor.colored(("[+] Enter Sha1 Hash Values: "),'white'))
start_time=time.time()
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/'
                       'master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt')
               .read(),'utf-8')
for password in passlist.split('\n'):
    hashguess=hashlib.sha1(bytes(password,'utf-8')).hexdigest()
    if hashguess==sha1hash:
        print(termcolor.colored((" [+] The password is: ",str(password)),'red'))
        end_time=time.time()
        print(termcolor.colored(("Total time needed: ",end_time-start_time),'blue'))
        quit()
    else:
        print(termcolor.colored((" [+] The password guess: ",str(password)," does not match,trying next.... "),'green'))
end_time1=time.time()
print("Password not in passwordlist!!!")
print(termcolor.colored(("Total time needed: ",end_time1-start_time),'green'))





