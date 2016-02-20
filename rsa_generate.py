#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto import Random
import sys

if len(sys.argv) <=1:
 print "Usage : rsa.generate.py <publickey.txt> <privatekey.txt>"
 exit() 
 
random_object = Random.new().read
rsa_object = RSA.generate(4096, random_object)
file1_object = open(sys.argv[1], "a+")
file1_object = open(sys.argv[1], "wb")
file1_object.write(rsa_object.publickey().exportKey())
file2_object = open(sys.argv[2], "a+")
file2_object = open(sys.argv[2], "wb")
file2_object.write(rsa_object.exportKey())
file1_object = open(sys.argv[1], "rb")
file1_object.read()
file2_object = open(sys.argv[2], "rb")
file2_object.read()
