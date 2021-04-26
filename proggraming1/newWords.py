import socket
import random

class words:

    def __init__(self):
        self.file = open("words.txt", "r")

        self.fileLines = self.file.read().split('\n')

        self.guesses = []
        self.guesses.append(self.fileLines[0])
        self.gsOptions = []
        del self.fileLines[-1]

    def findUppsetWord(self):
        word = self.fileLines[0]
        sameLetter = 0
        upsetWordSameLetter = 12
        upsetWord = ""

        for line in self.fileLines[1:-1]:

            sameLetter = 0
            for letter in line:
                if letter in word:
                    sameLetter += 1

            if sameLetter < upsetWordSameLetter:
                upsetWordSameLetter = sameLetter
                upsetWord = line
                print("word = " + word)
                print ("upsetWord = " + upsetWord + " with " + str(upsetWordSameLetter) + " same letter")

        self.guesses.append(upsetWord)

    def findSimilarWord(self, word):
        sameLetter = 0
        similarWordLetter = 0
        similarWord = ""

        for line in self.fileLines[1:-1]:

            if line == word:
                print("word is " + word + " and line is " + line)
                continue

            sameLetter = 0
            for letter in line:

                if letter in word:
                    sameLetter += 1

            if sameLetter > similarWordLetter:
                similarWordLetter = sameLetter
                similarWord = line
                print("word = " + word)
                print ("similar Word = " + similarWord + " with " + str(similarWordLetter) + " same letter")

            elif sameLetter >= 10:
                print("EQULE similar Word = " + similarWord + " with " + str(similarWordLetter) + " same letter")

        self.guesses.append(similarWord)

    def sendGuess(self, socket, port, guessNum):
        guess = random.choice(self.fileLines)
        print("i send - " + guess)
        socket.sendto(guess.encode(), ("tricky-guess.csa-challenge.com", port))
        rcvMsg = socket.recv(1024).decode("utf-8")
        print(rcvMsg)
        self.fileLines = list(filter(lambda a : len(set(guess).intersection(a)) == int(rcvMsg), self.fileLines))
        print ("len of lines = " + str(len(self.fileLines)))
        return int(rcvMsg)

    def updateGsOptions(self, list):
        bestGuess = self.guesses[list.index(max(list))]
        bestGuessLetter = max(list)
        print("best guess is " + bestGuess + "index is " + str(bestGuessLetter))

        sameLetter = 0

        for line in self.fileLines[1:-1]:

            if line == bestGuess:
                print("bestGuess is " + bestGuess + " and line is " + line)
                continue

            sameLetter = 0
            for letter in line:

                if letter in bestGuess:
                    sameLetter += 1

            if sameLetter >= bestGuessLetter:
                self.gsOptions.append(line)

        print (len(self.gsOptions))

    def removeLines(self, list):

        sameLetter = 0
        deleteNum = 0
        correctLetters = list[-1]
        bestWord = self.fileLines[len(list) - 1]
        print("last Word = " + bestWord)

        print("correct letters is : " + str(correctLetters))

        deleteNum = 0
        sameLetter = 0

        i = 0

        while i < len(self.fileLines):
        #for i in range(len(self.fileLines)):

            if i >= len(self.fileLines):
                print ("i = " + str(i) + " len  = " + str(len(self.fileLines)))
                break

            sameLetter = 0
            for letter in self.fileLines[i]:

                if letter in bestWord:
                    sameLetter += 1

            if sameLetter < correctLetters:
                del self.fileLines[i]
                deleteNum += 1
                i -= 1
            i += 1

        print("i delete = " + str(deleteNum) + " is stay " + str(len(self.fileLines)))