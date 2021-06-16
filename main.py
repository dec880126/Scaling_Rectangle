from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class Point(object):
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def distance(self, target):
        """
        type target: Point
        rtype: float
        """
        len_x = self.x - target.x
        len_y = self.y - target.y
        return sqrt(len_x ** 2 + len_y ** 2)
        
    def vector(self, target):
        """
        type target: Point
        rtype: list
        """
        dx = self.x - target.x
        dy = self.y - target.y
        return [dx, dy]
        
    def move_by(self, vector):
        """
        type vector: list
        """
        self.x += vector[0]
        self.y += vector[1]
        
    def show(self):
        """
        rtype: list
        """
        return [round(self.x, 2), round(self.y, 2)]
        
def vector_add(a, b):
    """
    type a, b: list
    rtype: list
    """
    return np.array(a) + np.array(b)
    
def vector_normalize(vector):
    """
    type vector: list
    rtype: list
    """
    length = sqrt(vector[0] ** 2 + vector[1] ** 2)
    return np.array(vector)/length

def vector_process(pa, pb, pc, pd, d1, d2, d3):
    """
    type a, b, c, d: Point
    type d1, d2, d3: float
    rtype: list
    """
    next1 = d1
    next2 = d2
    next3 = d3
    next = [next1, next2, next3]
    num = next.index(max(next))
    if num == 0:
        v_1 = vector_normalize(pa.vector(pc))
        v_2 = vector_normalize(pa.vector(pd))
    elif num == 1:
        v_1 = vector_normalize(pa.vector(pb))
        v_2 = vector_normalize(pa.vector(pd))
    elif num == 2:
        v_1 = vector_normalize(pa.vector(pb))
        v_2 = vector_normalize(pa.vector(pc))
    return v_1 + v_2

    
        
def main():
    #publish 4 point
    a = Point(-4, 2)
    b = Point(3, 4)
    c = Point(-3, -1)
    d = Point(4, 1)
    pointList = [a, b, c, d]
    print(f"a = {a.show()}, b = {b.show()}, c = {c.show()}, d = {d.show()}")

    # ----------Pre-graphing----------
    for point in pointList:
        plt.scatter(point.x, point.y, color = 'blue')

    # ----------Calculate the distance----------
    ab = ba = a.distance(b)
    ac = ca = a.distance(c)
    ad = da = a.distance(d)
    bc = cb = b.distance(c)
    bd = db = b.distance(d)
    cd = dc = c.distance(d)

    # ----------vector processing----------
    v_a = vector_process(a, b, c, d, ab, ac, ad)
    v_b = vector_process(b, a, c, d, ba, bc, bd)
    v_c = vector_process(c, a, b, d, ca, cb, cd)
    v_d = vector_process(d, a, b, c, da, db, dc)
    vectorList = [v_a, v_b, v_c, v_d]

    # ----------start the transformation----------
    for point, vector in zip(pointList, vectorList):
        point.move_by(vector)
        
    print("after transformation")
    print(f"a = {a.show()}, b = {b.show()}, c = {c.show()}, d = {d.show()}")

    # ----------Post-graphing----------
    for point in pointList:
        plt.scatter(point.x, point.y, color = 'red')
    plt.title("X-Y Figure")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()
        
    
if __name__ == '__main__':
    main()
