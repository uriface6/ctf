import socket
# for socket
import sys


def main():
    s = socket.socket()
    print("Socket successfully created")

    port = 2222

    s.connect(("tricky-guess.csa-challenge.com", port))
    f = open("words.txt", "r")

    lines = f.read().split('\n')
    print(len(lines))
    print(lines[0])

    list = []

    for x in range(16):
        rcvMsg = s.recv(1024).decode("utf-8")
        print(rcvMsg)
        if x != 0:
            list.append(int(rcvMsg))
        else:
            rcvMsg = s.recv(1024).decode("utf-8")
            print(rcvMsg)

        print("i send - " + lines[x])
        s.sendto(lines[x].encode(), ("tricky-guess.csa-challenge.com", port))

    s.close()

    print(list)

if __name__ == "__main__":
    main()
