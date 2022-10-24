#Variable scope, global variables
a = 5
print(a)

if (a < 10):
    b = 6      #Defined inside the block
    print(b)

print(b)       #Applicable outside the block

#Variable scope, local variables
def test():
    c = 20     #Local variable
    print(c)   #Can be used inside the block

test()
print(c)       #Can not be used ouside the block

def test2():
    global c   #Global variable
    c = 20
    print(c)   #Can be used inside the block

test2()
print(c)       #Applicable outside the block

#Incorrect order of conditions
y = 0;
if x < 30:
    y = y + 30
elif x < 20:
    y = y + 20
elif x < 10:
    y = y + 10
elif x < 5:
    y = y + 5
else:
    y = y +100

#Correct order of conditions
if x < 5:
    y = y + 5
elif x < 10:
    y = y + 10
elif x < 20:
    y = y + 20
elif x < 30:
    y = y + 30
else:
    y = y +100