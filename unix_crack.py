#coding:utf-8
#author:nothing
# import crypt
# from passlib.hash import sha512_crypt
# import hashlib
import passlib.hash
import new_crypt



test = 'root:$6$bdHK7Ubq$KR5wxI.zdgHSI8jS29N7HTMw.pttXuA4fhBbYWHUMxgjHyiql7MLOZx7tbsKrAqmUlQtsjEA37eQZDq8.UP/x1:17109:0:99999:7:::'
def testUnixPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dict.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = new_crypt.crypt(word,(salt))
        if(cryptWord == cryptPass):
            print '[+] Found Unix Password: ' + word + '\n'
            return
    print '[-] Unix Password Not Found!'
    return
def testLinuxPass(cryptPass):
    # print cryptPass
    salt = '${}${}$'.format('6',cryptPass.split("$")[2])
    dictFile = open('dict.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = new_crypt.crypt(word,(salt))
        if(cryptWord == cryptPass):
            print '[+] Found Linux Password: ' + word + '\n'
            return
    print '[-] Linux Password Not Found!'
    return

def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(":")[0]
            cryptPass = line.split(":",2)[1]
            print "[*] Cracking Password For : " + user
            testUnixPass(cryptPass)
            testLinuxPass(cryptPass)
if __name__ == '__main__':
    main()

