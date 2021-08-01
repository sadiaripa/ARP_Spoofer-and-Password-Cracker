import crypt
from termcolor import colored
def crackPass(cryptword):
    salt = cryptword[0:2]
    password_file=open("pass_word.txt",'r')
    for word in password_file.readlines():
        word=word.strip('\n')
        cryptPass= crypt.crypt(word,salt)
        if(cryptword==cryptPass):
            print(colored(("[+] Found Password: ",word),'green'))
            return

def main():
    global passFile
    passFile=open('username_pass.txt','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptword= line.split(':')[1].strip(' ').strip('\n')
            print(colored(("[+] Cracking Password For: ",user),'red'))
            crackPass(cryptword)


main()
