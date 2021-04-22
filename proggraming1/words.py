"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class words:

f = open("words.txt", "r")
count = 1
for x in f:
    if count > 10:
        break
    print(x)
    count += 1"""
import collections

f = open("words.txt", "r")
words = f.read().split('\n')
print(len(words))

abcDic = {}

duplicateDic = {
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0}

count = 0
upsetWord = ""
flag = False

for wrd in words[1:]:
    for lt in words[0]:
        if lt in

for word in words:
    for letter in word:
        count = 0
        for letter2 in word:
            if letter == letter2:
                 count += 1
        if count > 1:
            duplicateDic[count] += 1

        if letter in abcDic.keys():
            abcDic[letter] += 1
        else:
            abcDic[letter] = 1

print(abcDic)
orderDic = collections.OrderedDict(sorted(abcDic.items()))
print(orderDic)
print(duplicateDic)