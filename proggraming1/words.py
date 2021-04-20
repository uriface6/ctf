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

f = open("words.txt", "r")
lines = f.read().split('\n')
print(len(lines))
