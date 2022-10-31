#Factorial v1
n = 5
f = 1

while n > 1:
    f *= n
    n -= 1

print(f)

#Factorial v2
i = 2
n = 5
f2 = 1
while i <= n:
    f2 *= i
    i += 1

print(f2)

#Search for max
X = [1, 7, 10, -1]
xmax = X[0]
for x in X:
    #Update maximum
    if x > xmax:
        xmax = x

print(xmax)

#Search for min
X = [1, 7, 10, -1]
xmin = X[0]
for x in X:
    #Update minimum
    if x > xmin:
        xmin = x

print(xmin)

#Search for min and max
X = [1, 7, 10, -1]
xmax = X[0]
xmin = X[0]
for x in X:
    #Update maximum
    if x > xmax:
        xmax = x

    # Update minimum
    if x < xmin:
        xmin = x

print(xmin, xmax)

#List comprehensions
L = [1, 2, 3, 4, 5]

L2 = []
for l in L:
    L2.append(10*l)
print(L2)

L3 = [10 * l for l in L]
print(L3)

#Directory comprehensions
D = {'a' : 1, 'b' : 2, 'c' : 3}
D2 = {key:10*val for key, val in D.items()}
D3 = {val:key for key, val in D.items()}
print(D2)
print(D3)

#Search
a = 3

for l in L:
    if a == l:
        print('Found')
        break
else:
    print('Not found')

#Range
print(*range(10))
print(*range(13))
print(*range(10,100, 10))
print(*range(10,110, 10))
print(*range(50,110, 10))
print(*range(50,101, 10))
print(*range(50,100, 10))
print(*range(len(L)))

#Search for min, max and their indices
X = [1, 7, 10, -1]
xmax = X[0]
imax = 0
imin = 0
xmin = X[0]

for i in range(len(X)):
    #Update maximum and its index
    if X[i] > xmax:
        xmax = X[i]
        imax = i

    # Update minimum and its index
    if X[i] < xmin:
        xmin = X[i]
        imin = i

print(xmin, imin, xmax, imax)
