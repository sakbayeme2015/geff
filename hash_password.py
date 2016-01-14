#!/usr/bin/env python

import hashlib
import uuid
import sys

if len(sys.argv) <= 1:
 print "Usage python hash_funct.py <password>"
 exit()

def md5():
 salt = uuid.uuid4().hex  #Dictionnary attack
 password = sys.argv[1]
 hash_object = hashlib.md5(salt.encode() + password.encode()).hexdigest() 
 for i in password:
  return hash_object 

print "The password md5 hash file is :" , md5()

def sha1():
 salt = uuid.uuid4().hex
 password = sys.argv[1]
 hash_object = hashlib.sha1(salt.encode() + password.encode()).hexdigest()
 for i in password:
  return hash_object

print "The password sha1 hash file is :" , sha1()

def sha224():
 salt = uuid.uuid4().hex
 password = sys.argv[1]
 hash_object = hashlib.sha224(salt.encode() + password.encode()).hexdigest()
 for i in password:
  return hash_object
  
print "The password sha224 hash file is :" , sha224()

def sha256():
 salt = uuid.uuid4().hex
 password = sys.argv[1]
 hash_object = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
 for i in password:
  return hash_object

print "The password sha256 hash file is :" , sha256()

def sha384():
 salt = uuid.uuid4().hex
 password = sys.argv[1]
 hash_object = hashlib.sha384(salt.encode() + password.encode()).hexdigest()
 for i in password:
  return hash_object

print "The password sha384 hash file is :" , sha384()


def sha512():
 salt = uuid.uuid4().hex
 password = sys.argv[1]
 hash_object = hashlib.sha512(salt.encode() + password.encode()).hexdigest()
 for i in password:
  return hash_object

print "The password sha512 hash file is :" , sha512()
