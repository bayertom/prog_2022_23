import os

#Open and close file
# path = 'C:/Tomas/Tex/test.txt'  #Incorrect path
path = 'C:/Tomas/Text/test.txt'
f = open(path)
f.close()
#  f = open(path,'rt')

#File operation, using exceptions
try:
    f = open(path)
except IOError as e:
    print(e)
finally:
    f.close()
print('Monday')

#Properties of the open file
f.closed
f.mode
f.writeable()

#More comfortable Python-like approach, read
with open(path) as f:
    data = f.read(10)
    print(data)
    data = f.read(10)
    print(data)

#Readline
with open(path) as f:
    #for ch in data:
 #    print(ch)
    data = f.readline()
    print(data)
    data = f.readline()
    print(data)
    data = f.readline()
    print(data)

#Radline, process entire file
with open(path) as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)

#Common approach with readlines
with open(path) as f:
    lines = f.readlines()
    print(lines)
    print(lines[2])

#Shifts over the open file
path = 'C:/Tomas/Text/test.txt'
f = open(path)
f.tell()
data = f.read(5)
f.tell()
data = f.read(10)
f.tell()
data = f.read(5)
f.tell()
data = f.read()
f.tell()
f.seek(5,0)
f.tell()
f.seek(5)
f.tell()
f.seek(15,0)
f.tell()
f.seek(5)
f.tell()
f.seek(5,1)

#Write into the file
path = 'C:/Tomas/Text/test28.txt'
with open(path, 'r+') as f:
    data = f.readline()
    print(data)
    f.write('\nI like football')

#Open binary file
path = 'C:/Tomas/Text/picture.png'
f = open(path,'rb')
data = f.read()
print(data)
for b in data:
    print(b)
    print(b)

