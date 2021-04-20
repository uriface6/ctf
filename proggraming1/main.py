# An example script to connect to Google using socket
# programming in Python
import socket  # for socket
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

    for x in range(16):
        print(s.recv(1024).decode("utf-8"))

        """input_msg = s.recv(1024)
        full_msg = input_msg.split('\n')
        for j in full_msg:
            print(j)"""

        print("i send - " + lines[x])
        #s.send(lines[x])
        s.sendto(lines[x].encode(), ("tricky-guess.csa-challenge.com", port))

    s.close()
    """s.bind(('', port))
    print ("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(5)
    print ("socket is listening")

    while True:

        # Establish connection with client.
        c, addr = s.accept()
        print ('Got connection from', addr)

        # send a thank you message to the client.
        c.send('Thank you for connecting')

    # Close the connection with the client
    c.close()"""


if __name__ == "__main__":
    main()
