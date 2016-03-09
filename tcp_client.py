#!/usr/bin/env python

import socket 

target_host = "127.0.0.1"
target_port = 9999
data = "GET / HTTP/1.1/\r\nHost: google.com\r\n\r\n"

def tcp_client():
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect((target_host,target_port))
 client.send(data)
 response = client.recv(4096)
 print response

if __name__ == "__main__" :
 tcp_client()
