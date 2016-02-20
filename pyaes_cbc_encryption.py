#!/usr/bin/env python

import pyaes
import sys

if len(sys.argv) <= 1:
 print "Usage : pyaes_cbc_encryption.py <original_file.txt> < output_encrypt_file.txt>"
 print "Exemple : key = 16 bits , file = 16 strings"
 exit()

n = 16
key = "0123456789abcdef"
file1_object = open(sys.argv[1] , "rb")
contents = file1_object.read(n)
file2_object = open(sys.argv[2] , "a+")
file3_object = open(sys.argv[2] , "wb")
object_encrypt = pyaes.AESModeOfOperationCBC(key , "this is an IV456")
file3_object.write(object_encrypt.encrypt(contents))
file3_object = open(sys.argv[2] , "rb")
file3_object.read(n)
