import hashlib
import termcolor
hashvalue = input("[+] Enter a string to hash: ")
hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print(termcolor.colored((hashobj1.hexdigest()),'red'))

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print(termcolor.colored((hashobj2.hexdigest()),'red'))

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print(termcolor.colored((hashobj3.hexdigest()),'red'))
hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print(termcolor.colored((hashobj4.hexdigest()),'red'))
hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print(termcolor.colored((hashobj5.hexdigest()),'red'))