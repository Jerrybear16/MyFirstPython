

#print your name

print("Jeroen")

#print the lyrics to a song

stairway = "There's a lady who's sure, all that glitters is gold, and she's buying a stairway to heaven"

print("stairway")

#display several numbers

x=1
print(x)
x=2
print(x)
x=3
print(x)

#solve the equation

print(64+32)

#same but with variables

x = 64
y = 32
z = x+y
print(z)

#print lucky in s

print("%s" % "lucky")

#print date

print("today is %d/%d/%d"% (2,2,2016))

#replace

string = "hello world"
print(string)
string =string.replace("hello","world")
print(string)
string =string.replace("world","hello")
print(string)
string = string.replace("world","hello world, this is Jeroen")
print(string)
string = "hello world, this is jeroen"
string =string.replace("hello world","suh dude")
print(string)

#find

print(string.find("Suh"))
string = string.replace("dude","suh")
print(string)
print(string.find("jeroen"))


#string join

strlist = ["one","two", "three"]
liststr = ","
liststr = liststr.join(strlist)
print(liststr)

#string split

liststr2 = liststr.split(",")
print(liststr)

#random numbers

import random

x = random.randint(0,9)
print(x)
x = random.randint(0,9)
print(x)
x = random.randint(0,9)
print(x)


#keyboard input

print("\na break in the output to make it look nice\n\n")

phoneNumber = input("Input a phone number: ")
print(phoneNumber)

language = input("Input your favorite language: ")
print(language)

#ifs

numInRange = int(input("Give me a number between 1 and 10: "))

if numInRange <1 or numInRange >10:
  print("invalid number")

#for loops

clist = ['Canada','USA','Mexico','Australia']
for country in clist:
  print(country)

#while loops
i =0
while i < len(clist):
  print(clist[i])
  i+=1

numList = [1,2,3,4,5]

def sum(nl):
  s = 0
  for int in nl:
    s+=int
  return s

print(sum(numList))

#lists

print("I'm not making a list of 50 items i'm sorry")


#list opperations

y = [6,4,2]
y.append(12)
y.append(8)
y.append(4)
print(y)

y[1] = 3
print(y)

#range function

longList = []

for x in range(1000):
  longList.append(x)
#print(longList)


#dictionary

cDict = { "United States of America":"US", "Canada":"CAN"}
print(cDict)

#read File

"""
file = open("textfile.txt",'r')

print(file.read())

file = open("fakefile.txt",'r')
print(file.read())

file = open("textfile.txt",'w')
file.write("take it easy")

file.close()
"""
import datetime

date = datetime.datetime.now()

print(date)

