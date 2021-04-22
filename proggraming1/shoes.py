import requests
import socket

s = socket.socket()
print("Socket successfully created")

port = 80

s.connect(("192.115.211.70", port))
s.sendall("""GET/ubuntu/dists/bionic/InRelease HTTP/1.1 
Host: il.archive.ubuntu.com
Cache-Control: max-age=0
Accept: text/*
If-Modified-Since: Thu, 26 Apr 2018 23:38:40 GMT
User-Agent: Debian APT-HTTP/1.3 (1.6.12)""".encode())

"""RT5'®/EúêR@@¯â
GET /ubuntu/dists/bionic/InRelease HTTP/1.1
Host: il.archive.ubuntu.com
Cache-Control: max-age=0
Accept: text/*
If-Modified-Since: Thu, 26 Apr 2018 23:38:40 GMT
User-Agent: Debian APT-HTTP/1.3 (1.6.12)"""


rcvMsg = s.recv(1024).decode("utf-8")
print(rcvMsg)

"""r = requests.get("ec2-52-28-255-56.eu-central-1.compute.amazonaws.com")
print(r.text())"""