#Recursion
def f(n):
    print("C(" + str(n)+")")
    if (n == 1):
        print("D");
    else:
        print("f(" + str(n-1) + ")")
        f(n - 1)
    print("E(" + str(n) + ")")

f(3)

#Factorial 1
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

#Factorial 2
def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1

factorial = fact(3)

#Fibonacci number
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

#fibo = fib(10)
#print(fibo)

#Recursion, problem 1
def alfa(n):
    if n > 1:
        return n * alfa(n+1)
    else:
        return 1

#al = alfa(2)

#Recursion, problem 2
def beta(n):
    if n == 1:
        return 1
    else:
        return n * beta(n-2)

be = beta(2)

#Find maximum
def maximum(X, l, r):
    #Recursive solution
    if r - l > 1:
        #Median
        m = (l + r) // 2

        #Process left part
        max1 = maximum(X, l, m)

        #Process right part
        max2 = maximum(X, m+1, r)

        #Find maximum of both
        return max(max1, max2)

    #Non-recursive solution
    else:
        return max(X[l], X[r])

X = [5, 6, 13, -8, 19]
print(maximum(X, 0, len(X)-1))


def bSearch(a, x, l, r):

    #Element not found
    if (l > r):
       return -1

    #Mid index
    m = (l + r)//2

    #Element found
    if a == x[m]:
       return m

    #Process left part
    if a < x[m]:
       return bSearch(a, x, l, m - 1)

    #Process right part
    else:
       return bSearch(a, x, m + 1, r )

print(search(X, 0, len(X)-1, 19))