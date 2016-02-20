#!/usr/bin/env python

from Crypto.Cipher import AES
import sys

if len(sys.argv) <= 1:
 print "Usage : aes_cbc_decryption.py <encrypting_file.txt> < output_decrypting_file.txt>"
 exit()

n = 32
key = "0123456789abcdef0123456789abcdef"
file1_object = open(sys.argv[1] , "rb")
contents = file1_object.read(n)
file2_object = open(sys.argv[2] , "a+")
file3_object = open(sys.argv[2] , "wb")
object_encrypt = AES.new(key , AES.MODE_CBC , "this is an IV456")
file3_object.write(object_encrypt.decrypt(contents))
file3_object = open(sys.argv[2] , "rb")
file3_object.read(n)
