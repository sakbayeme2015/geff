#!/usr/bin/env python

import hashlib
import sys

if len(sys.argv) <= 1:
 print "Usage : python programme.py <path of file>"
 print "Exemple : python funch_sha.py /home/file.txt"
 exit()

def md5():
 BLOCKSIZE = 65535
 file_object = open(sys.argv[1] , "rb")
 hash_object = hashlib.md5()
 buffer = file_object.read(BLOCKSIZE)
 for i in buffer:
  hash_object.update(i)
  i = file_object.read(BLOCKSIZE)
  return hash_object.hexdigest()

print "The md5 sum is :" , md5()

def sha1():
 BLOCKSIZE = 65535
 file_object = open(sys.argv[1] , "rb")
 hash_object = hashlib.sha1()
 buffer = file_object.read(BLOCKSIZE)
 for c in buffer:
  hash_object.update(c)
  c = file_object.read(BLOCKSIZE)
  return hash_object.hexdigest()

print "The sha1 sum is :" , sha1()

def sha224():
 BLOCKSIZE = 65535
 file_object = open(sys.argv[1] , "rb")
 hash_object = hashlib.sha224()
 buffer = file_object.read(BLOCKSIZE)
 for d in buffer:
  hash_object.update(d)
  d = file_object.read(BLOCKSIZE)
  return hash_object.hexdigest()

print "The sha224 sum is :" , sha224()

def sha256():
 BLOCKSIZE = 65535
 file_object = open(sys.argv[1] , "rb")
 hash_object = hashlib.sha256()
 buffer = file_object.read(BLOCKSIZE)
 for e in buffer:
  hash_object.update(e)
  e = file_object.read(BLOCKSIZE)
  return hash_object.hexdigest()

print "The sha256 sum is :" , sha256()

def sha384():
 BLOCKSIZE = 65535
 file_object = open(sys.argv[1] , "rb")
 hash_object = hashlib.sha384()
 buffer = file_object.read(BLOCKSIZE)
 for a in buffer:
  hash_object.update(a)
  a = file_object.read(BLOCKSIZE)
  return hash_object.hexdigest()

print "The sha384 sum is :" , sha384()

def sha512():
 BLOCKSIZE = 65535
 file_object = open(sys.argv[1] , "rb")
 hash_object = hashlib.sha512()
 buffer = file_object.read(BLOCKSIZE)
 for z in buffer:
  hash_object.update(z)
  z = file_object.read(BLOCKSIZE)
  return hash_object.hexdigest()

print "The sha512 sum is :" , sha512()
