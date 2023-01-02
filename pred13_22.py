from copy import deepcopy
from operator import attrgetter

#Rodicovska trida
class GO:
    def __init__(self, color=0, level=0, width=0):
        self._color = color
        self._level = level
        self._width = width

    def print(self):
        print("Color =" + str(self._color) + ", Level =" + str(self._level) + ", Width=" + str(self._width))

#Odvozena trida
class Point(GO):
    # Datova polozka tridy
    counter = 0

    # Inicializator
    def __init__(self, color=0, level=0, width=0, x=0, y=0):
        # Inicializator GO
        super().__init__(color, level, width)

        # Datove polozky objektu
        self.__id = Point.counter
        self.__x = x
        self.__y = y

        # Inkrementace datove polozky tridy
        Point.counter = Point.counter + 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def print(self):
        print("\nPoint, graphical + geometetric properties:")
        super().print()
        print("ID =" + str(self.__id) + ", X =" + str(self.__x) + ", Y=" + str(self.__y))


    def __lt__(self, other):
        return self.__x < other.__x

    def __eq__(self, other):
       return (self.__x == other.__x) and (self.__y == other.__y)

#Comparator
def distance(q, p):
    dx = q.x - p.x
    dy = q.y - p.y
    return (dx * dx + dy * dy)**0.5

#Objekt tridy GO a volani metody print
go = GO(10, 20, 30)
go.print()

#Objekt odvozene tridy Point a volani metody print
p1 = Point(10, 20, 30, 100.1, 200.2)
p1.print()
p2 = Point(10, 20, 30, 0, 0)
p2.print()

#Generalizace, spolecne zaschazeni s objekty
G = [go, p1, p2]

for g in G:
    g.print()

#Shallow copy
print(id(p1))
p3 = p1
print(id(p3))

#Deep copy
p4 = deepcopy(p1)
print(id(p4))

p1.x = 127
p1.print()
p3.print()
p4.print()
p1.x = 100.1

#Operator < (__lt__)
print(10 < 20)
print('C' < 'A')
print(p1 > p4)

#Operator == (__eq__)
print(10 == 10)
# Bez implementovaneho __eq__ porovnava, zda se jedna o stejny objekt (false)
# S implementovanym __eq__ porovnava souradnice obou bodu (true)
print(p1 == p4)

#Trideni kolekci, ruzne varinty
P = [p1, p2, p3, p4]
P.sort(reverse=True)

for p in P:
    p.print()

P.sort(key = lambda k : k.y)
P.sort(key= attrgetter('y'))
for p in P:
    p.print()

#Trideni kolekci, vlastni comparator
q = Point(10, 20, 30, 0, 0)
P.sort(key = lambda k : distance(k, q))
for p in P:
    p.print()