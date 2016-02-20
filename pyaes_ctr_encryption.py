#!/usr/bin/env python

import pyaes
import sys
import os
import hashlib


if len(sys.argv) <=1:
 print "Usage : ./pyaes_ctr_encryption <original_file.txt> <encrypt_output.txt>"
 exit()

key = "efda20e3840bf2eca3e5b116ea659ef3"
filesize = os.path.getsize(sys.argv[1])
file1_object = open(sys.argv[1], "rb")
contents = file1_object.read(filesize)
file2_object = open(sys.argv[2], "a+")
file3_object = open(sys.argv[2], "wb")
object_encrypt = pyaes.AESModeOfOperationCTR(key)
file3_object.write(object_encrypt.encrypt(contents))
file3_object = open(sys.argv[2], "rb")
file3_object.read(filesize)
