#!/usr/bin/env python

from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import sys

if len(sys.argv) <=2:
 print "Usage : pkcs1_v1_5.py <cleartext> <output_encrypt.txt>"
 print "Usage : generate publickkey and privatekey before "
 exit()

file_object = open(sys.argv[1], "rb")
contents = file_object.read()
key_object = RSA.importKey(open("/root/publickkey.txt").read()) 
sha_object = SHA.new(sys.argv[1])
object_encrypt = PKCS1_v1_5.new(key_object)
file1_object = open(sys.argv[2], "a+")
file1_object = open(sys.argv[2], "wb")
file1_object.write(object_encrypt.encrypt(contents+sha_object.digest()))
file1_object = open(sys.argv[2], "rb")
file1_object.read()
