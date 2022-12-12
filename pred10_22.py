class Point:

    counter = 0

    def __init__(self, x_ = 0, y_ = 0):
       self.id = Point.counter
       self.x = x_
       self.y = y_
       Point.counter += 1

    def Print(self):
        print("ID:" + str(self.id) + ", x=" +str(self.x) + ", y=" + str(self.y) + "\n" )


class Algorithms:

    def euclDistance(self, p1 , p2 ):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        d = (dx*dx + dy * dy) **0.5

        return d

    def euclDistance2(p1 , p2 ):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        d = (dx*dx + dy * dy) **0.5

        return d

p1 = Point()
p2 = Point(30,-70)
p3 = Point(10,10)
p1.Print()
p2.Print()
p3.Print()

a = Algorithms()
dist = a.euclDistance(p1, p2)
print(dist)
