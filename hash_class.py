#!/usr/bin/env python

import hashlib

class md5():
 def __init__(self, password, hashing):
  self.password = password
  self.hashing = hashing
 def pass_file(self, password):
  self.password = password
 def hash_file(self, hashing):
  self.hashing = hashing
  return pass_object.hash_file

class sha1():
 def __init__(self, password1, hashing1):
  self.password1 = password1
  self.hashing1 = hashing1
 def pass_file1(self, password1):
  self.password1 = password1
 def hash_file1(self, hashing1):
  self.hashing1 = hashing1
  return pass_object1.hash_file1

class sha256():
 def __init__(self, password2, hashing2):
  self.password2 = password2
  self.hashing2 = hashing2
 def pass_file2(self, password2):
  self.password2 = password2
 def hash_file2(self, hashing2):
  self.hashing2 = hashing2
  return pass_object2.hash_file2

class sha512():
 def __init__(self, password3, hashing3):
  self.password3 = password3
  self.hashing3 = hashing3
 def pass_file3(self, password3):
  self.password3 = password3
 def hash_file3(self, hashing3):
  self.hashing3 = hashing3
  return pass_object3.hash_file3

pass_object = md5("password", "hashing")
pass_object1 = sha1("password1", "hashing1")
pass_object2 = sha256("password2", "hashing2")
pass_object3 = sha512("password3", "hashing3")
pass_object.pass_file = raw_input(b"Enter Password : ")
pass_object.hash_file = hashlib.md5(pass_object.pass_file.encode()).hexdigest() 
pass_object1.hash_file1 = hashlib.sha1(pass_object.pass_file.encode()).hexdigest() 
pass_object2.hash_file2 = hashlib.sha256(pass_object.pass_file.encode()).hexdigest()
pass_object3.hash_file3 = hashlib.sha512(pass_object.pass_file.encode()).hexdigest()

print pass_object.hash_file
print pass_object1.hash_file1
print pass_object2.hash_file2
print pass_object3.hash_file3

