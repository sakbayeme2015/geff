#!/usr/bin/env python

import pyaes
import os
import sys

if len(sys.argv) <= 1:
 print "Usage : pyaes_cbc_decrypt_feeder.py < encrypt_file.txt> <Output_file_decrypt.txt>"
 exit()

key = "0123456789abcdef0123456789abcdef"
filesize = os.path.getsize(sys.argv[1])
file1_object = open(sys.argv[1] ,"rb")
contents = file1_object.read(filesize)
file2_object = open(sys.argv[2] , "a+")
file3_object = open(sys.argv[2] , "wb")
object_encrypt = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key , "this is an IV456"))
file3_object.write(object_encrypt.feed(contents))
file3_object = open(sys.argv[2] , "rb")
file3_object.read(filesize)
