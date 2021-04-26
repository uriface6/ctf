import socket
# for socket
import sys
from newWords import words


def main():
    s = socket.socket()
    print("Socket successfully created")

    port = 2222

    s.connect(("tricky-guess.csa-challenge.com", port))

    wordsFile = words()
    print(len(wordsFile.fileLines))

    list = []

    wordsFile.findUppsetWord()

    print (wordsFile.guesses)
    counter = 0

    #print the cat
    rcvMsg = s.recv(1024).decode("utf-8")
    print(rcvMsg)
    #print GO!
    rcvMsg = s.recv(1024).decode("utf-8")
    print(rcvMsg)
    #send first guess

    for i in range(15):
        list.append(wordsFile.sendGuess(s, port, i))
        #print()
        #list.append(i + 4)
        #wordsFile.removeLines(list)


    #if for 3 guess
    """sendWord = ""
    if list[0] > list[1]:
        wordsFile.findSimilarWord(wordsFile.guesses[0])
    else:
        wordsFile.findSimilarWord(wordsFile.guesses[1])

    #send guess 3
    list.append(wordsFile.sendGuess(s, port, 2))

    wordsFile.updateGsOptions(list)"""

    s.close()

    print(list)

if __name__ == "__main__":
    main()






    """for guess in wordsFile.guesses:

        rcvMsg = s.recv(1024).decode("utf-8")
        print(rcvMsg)
        if counter != 0:
            list.append(int(rcvMsg))
        else:
            rcvMsg = s.recv(1024).decode("utf-8")
            print(rcvMsg)


        print("i send - " + guess)
        s.sendto(guess.encode(), ("tricky-guess.csa-challenge.com", port))

        counter += 1

    rcvMsg = s.recv(1024).decode("utf-8")
    print(rcvMsg)
    list.append(int(rcvMsg))
    """