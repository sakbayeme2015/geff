#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import sys

if len(sys.argv) <=1:
 print "Usage : pkcs1_v1_5_decrypt.py <encryptfile.txt> < output_decrypt.txt>"
 exit()

file1_object = open(sys.argv[1], "rb")
contents = file1_object.read()
key_object = RSA.importKey(open("/root/privatekey.txt").read())
sha_object = SHA.new(sys.argv[1])
object_encrypt = PKCS1_v1_5.new(key_object)
file2_object = open(sys.argv[2], "a+")
file2_object = open(sys.argv[2], "wb")
file2_object.write(object_encrypt.decrypt(contents , sha_object))
file2_object = open(sys.argv[2], "rb")
file2_object.read()
