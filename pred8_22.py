import math

def getRadius(perimeter):
    if perimeter >= 0:
        return perimeter /(2*pi)
    else:
        return -1


r = getRadius(-1)
if (r>=0):
    print('do something')

def getRadius2(perimeter):
    if perimeter >= 0:
        return perimeter /(2*pi)
    else:
        raise ValueError('Perimeter must be positive', perimeter)

#r = getRadius2(-1)

def f1(a, b):
    if b == 0:
        return -1
    if a * b < 0:
        return -2
    return (a/b)**0.5

a = 1; b = 2;
print(f1(a, b))
a = 1; b = 0;
print(f1(a, b))
a = 1; b = -2;
print(f1(a, b))
#a = 1; b = [2];
print(f1(a, b))

def f2(a, b):
    try:
        return (a / b) ** 0.5
    except ZeroDivisionError:
        return -1
    except ValueError:
        return -2
    except Exception:
        return -3

print(f2(a, b))
a = 1; b = 0;
print(f2(a, b))
a = 1; b = -2;
print(f2(a, b))
#a = 1; b = [2];
print(f2(a, b))

def f3(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError('Incorrect type:', type(a), type(b))
    if b==0:
        raise ZeroDivisionError('Divison by zero', b)
    if a * b < 0:
        raise ValueError('Complex solution', a, b)

    return (a / b) ** 0.5

try:
    f3(1, 2)
    #f3(1, 0)
    #f3(1, -2)
    #f3(1, [2])
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)


def f4(a, b):
    try:
        return (a / b) ** 0.5

    except TypeError as e:
        raise e

    except ZeroDivisionError as e:
        raise e

    except Valuesrror as e:
        raise e

try:
    f4(1, 2)
    f4(1, 0)
    f4(1, -2)
    f4(1, [2])
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    f4(1, 2)
    f4(1, 0)
    f4(1, -2)
    f4(1, [2])
except Exception as e:
    print(e)