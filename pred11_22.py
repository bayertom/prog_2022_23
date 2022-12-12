
#Class with encapsulation
class Point:

    __counter = 0

    def __init__(self, x_ = 0, y_ = 0):
        #Restric access to private
        self.__id = Point.__counter
        self.__x = x_
        self.__y = y_
        Point.__counter += 1

    #Getters
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getXY(self):
        return self.__x, self.__y

    def Print(self):
        print("ID:" + str(self.__id) + ", x=" +str(self.__x) + ", y=" + str(self.__y) + "\n" )

    #Setters
    def setX(self, x_):
        self.__x = x_

    def setY(self, y_):
        self.__y = y_

    def setXY(self, x_, y_):
        self.__x = x_
        self.__y = y_

    #Properties
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x_):
        self.__x = x_

    @y.setter
    def x(self, y_):
        self.__y = y_

#Getters and setters
p1 = Point()
x1 = p1.getX()
y1 = p1.getY()
x1, y1 = p1.getXY()
p1.Print()
p1.setX(127)
p1.setY(255)

#Properties
x1 = p1.x
y1 = p1.y
p1.Print()
p1.x = 5

#Passing objects as parameters
class Algorithms:

    def euclDistance(self, p1 , p2 ):
        dx = p2.getX() - p1.getX()
        dy = p2.y - p1.y

        d = (dx*dx + dy * dy) **0.5

        return d

    def midPoint(self, p1, p2):
        xmid = 0.5 * (p1.x + p2.x)
        ymid = 0.5 * (p1.y + p2.y)
        return Point(xmid, ymid)

    @staticmethod
    def euclDistance2(p1 , p2 ):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        d = (dx*dx + dy * dy) **0.5

        return d

# Distance between two points
p1 = Point(0, 0)
p2 = Point(10, 10)

a = Algorithms()
dist = a.euclDistance(p1, p2)

#Create midpoint
pmid = a.midPoint(p1, p2)
pmid.Print()

#Static method
dist2 = Algorithms.euclDistance2(p1, p2)
print(dist2)

#Composition
class Line:
    def __init__(self, p1_, p2_):
        self.__p1 = p1_
        self.__p2 = p2_

    def Print(self):
        self.__p1.print()
        self.__p2.print()

#Create line using the composotion
l = Line(p1, p2)
l.Print()