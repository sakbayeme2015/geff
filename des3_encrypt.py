#!/usr/bin/env python

from Crypto.Cipher import DES3
import os
import sys

if len(sys.argv) <=1:
 print "Usage : ./des3_decrypt.py </path/encrypt_file.txt> </path/decrypt_file.txt>"
 exit()

filesize = os.path.getsize(sys.argv[1])
key = "0123456789abcdef"
file_object = open(sys.argv[1], "rb")
contents = file_object.read()
object_encrypt = DES3.new(key, DES3.MODE_CFB)
file1_object = open(sys.argv[2], "a+")
file1_object = open(sys.argv[2], "wb")
file1_object.write(object_encrypt.decrypt(contents))
file1_object = open(sys.argv[2], "rb")
file1_object.read()

