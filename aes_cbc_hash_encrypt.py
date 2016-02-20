#!/usr/bin/env python

from Crypto.Cipher import AES
import hashlib
import sys
import uuid

if len(sys.argv) <= 1:
 print "Usage : aes_cbc_hash_md5.py <original_file.txt> <output_encrypt.txt>"
 exit()

n = 32
key = "2c21bf0b0e1a45586bb2a56679a5269e"
file1_object = open(sys.argv[1], "rb")
contents = file1_object.read(n)
file2_object = open(sys.argv[2], "a+")
file3_object = open(sys.argv[2], "wb")
object_encrypt = AES.new(key , AES.MODE_CBC , "this is an IV456")
file3_object.write(object_encrypt.encrypt(contents))
file3_object = open(sys.argv[2], "rb")
file3_object.read(n)
