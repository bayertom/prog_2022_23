#Immutable object
x=10
id(x)
type(x)

#New variable
x = 5
id(x)
x=x+5
id(x)

#Mutable object
L=[1, 2, 3, 4]
id(L)
L[0]=10
id(L)

#Return 1 parameter
def add(a, b):
    return a + b

s = add(4, 5)
print(s)

#Return 2 parameters
def add_subtract(a, b):
    return a + b, a - b

a,s = add_subtract(4, 5)
print(a, s)

#Return 0 parameters
def add_subtract2(a, b):
    r1, r2 = a + b, a - b
    print(r1, r2)

add_subtract2(4, 5)

#Immutable object
def f(x):
    x = 7
    print(id(x))
    print(x)

c = 10
print(c)
print(id(c))
f(c)
print(c)

#Mutable object
def f2(L):
    L[0] = 7
    print(id(L))
    print(L)

L = [1, 2, 3, 4]
print(L)
print(id(L))
f2(L)
print(L)

#Default parameters
def distance(dx = 10, dy = 20):
    return (dx*dx + dy * dy)**0.5

dx1 = 3
dy1 = 4
d1 = distance(dx1, dy1)
print(d1)
d2 = distance(dx1)
print(d2)

#Positional arguments, list
def sum(*L):
    s = 0
    for l in L:
        s += l
    return s

#Positional arguments, directory
def printDict(**D):
    for d in D:
        print(d, D[d])

s = sum(1, 3, 5, 7, 9)
printDict(name = 'Jan', age = 25)

#Factorial
def factorial(n):
    #Factorial v1
    f = 1

    while n > 1:
        f *= n
        n -= 1
    return f

#Passing function as a formal parameter
def combination(n, k, f):
    num = f(n)
    denom = f(n-k) * f(k)
    return num / denom

print(factorial(5))
print(combination(5, 1, factorial))

#Curent approach
def combination2(n, k):
    num = factorial(n)
    denom = factorial(n-k) * factorial(k)
    return num / denom

print(combination2(5, 1))
