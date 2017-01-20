# encoding: utf-8
# module crypt
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/crypt.so
# by generator 1.144
# no doc
# no imports

# coding=utf-8
__author__ = 'pengchong.lee'

import passlib.hash
import re

ALGORITHM_MAPPER = {
    1: passlib.hash.md5_crypt,
    5: passlib.hash.sha256_crypt,
    6: passlib.hash.sha512_crypt
}


def crypt(word, salt):
    standard_salt = re.compile('\s*\$(\d+)\$([\w\./]*)\$')
    match = standard_salt.match(salt)
    if not match:
        return ValueError("salt format is not correct, "
                         "in D:\Python27\Lib\site-packages\crypt.py")
    algorithm_num = match.group(1)
    extra_str = match.group(2)
    entryptor = ALGORITHM_MAPPER.get(int(algorithm_num))
    if int(algorithm_num) == 1:
        result = entryptor.encrypt(word, salt=extra_str)
    else:
        result = entryptor.encrypt(word, salt=extra_str, rounds=5000)
    return result
