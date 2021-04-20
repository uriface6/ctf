# An example script to connect to Google using socket
# programming in Python
import socket  # for socket
import sys

def main():
    s = socket.socket()
    print ("Socket successfully created")

    port = 2222

    s.connect(("tricky-guess.csa-challenge.com", port))

    for i in xrange(15):
        print(s.recv(1024))
        s.send("abc")

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