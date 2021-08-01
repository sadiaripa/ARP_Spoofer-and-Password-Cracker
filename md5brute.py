from termcolor import colored
import hashlib

def tryopen(word_list):
    global pass_file
    try:
        pass_file=open(word_list,"r")
    except:
        print("No such file at that path!!!")
        quit()
pass_hash=input(colored(("[+] Enter MD5 Hash Value: "),'green'))
word_list=input(colored(("[+] Enter path to the password file: "),'green'))
tryopen(word_list)
for word in pass_file:
    print(colored(("[+] Trying:  ",word.strip("\n")),'red'))
    enc_word=word.encode("utf-8")
    md5digest=hashlib.md5(enc_word.strip()).hexdigest()
    if md5digest==pass_hash:
        print(colored(("[+] Password Found ",word),'green'))

        exit(0)
print("[+] Password not in list")
