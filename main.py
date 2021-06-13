#coding=utf-8
#
#
from math import sqrt
import numpy as np

class Point(object):
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def distance(self, target) -> int:
        len_x = self.x - target.x
        len_y = self.y - target.y
        return sqrt(len_x ** 2 + len_y ** 2)
        
    def vector(self, target: Point) -> list:
        dx = self.x - target.x
        dy = self.y - target.y
        return [dx, dy]
        
    def move_by(self, vector: list):
        self.x += vector[0]
        self.y += vector[1]
        
    def show(self):
        return [self.x, self.y]
        
def vector_add(a: list, b: list) -> list:
    return np.array(a) + np.array(b)
    
def vector_normalize(vector: list) -> list:
    length = sqrt(vector[0] ** 2 + vector[1] ** 2)
    return np.array(vector)/length
    
        
def main():
    #publish 4 point
    a = Point(1, 1)
    b = Point(3, 1)
    c = Point(1, 2)
    d = Point(3, 2)
    print(f"a = {a.show()}, b = {b.show()}, c = {c.show()}, d = {d.show()}")
    ab = ba = a.distance(b)
    ac = ca = a.distance(c)
    ad = da = a.distance(d)
    bc = cb = b.distance(c)
    bd = db = b.distance(d)
    cd = dc = c.distance(d)
    #----------case a----------
    a_next = [ab, ac, ad]
    num = a_next.index(max(a_next))
    if num == 0:
        v_ca = vector_normalize(a.vector(c))
        v_da = vector_normalize(a.vector(d))
        v_a = vector_add(v_ca, v_da)
    elif num == 1:
        v_ba = vector_normalize(a.vector(b))
        v_da = vector_normalize(a.vector(d))
        v_a = vector_add(v_ba, v_da)
    elif num == 2:
        v_ba = vector_normalize(a.vector(b))
        v_ca = vector_normalize(a.vector(c))
        v_a = vector_add(v_ba, v_ca)
    #----------case b----------
    b_next = [ba, bc, bd]
    num = b_next.index(max(b_next))
    flag_b = -1
    if num == 0:
        v_cb = vector_normalize(b.vector(c))
        v_db = vector_normalize(b.vector(d))
        v_b = vector_add(v_cb, v_db)
    elif num == 1:
        v_ab = vector_normalize(b.vector(a))
        v_db = vector_normalize(b.vector(d))
        v_b = vector_add(v_ab, v_db)
    elif num == 2:
        v_ab = vector_normalize(b.vector(a))
        v_cb = vector_normalize(b.vector(c))
        v_b = vector_add(v_ab, v_cb)
    #----------case c----------
    c_next = [ca, cb, cd]
    num = c_next.index(max(c_next))
    flag_c = -1
    if num == 0:
        v_bc = vector_normalize(c.vector(b))
        v_dc = vector_normalize(c.vector(d))
        v_c = vector_add(v_bc, v_dc)
    elif num == 1:
        v_ac = vector_normalize(c.vector(a))
        v_dc = vector_normalize(c.vector(d))
        v_c = vector_add(v_ac, v_dc)
    elif num == 2:
        v_ac = vector_normalize(c.vector(a))
        v_bc = vector_normalize(c.vector(b))
        v_c = vector_add(v_ac, v_bc)
    #----------case d----------
    d_next = [da, db, dc]
    num = d_next.index(max(d_next))
    if num == 0:
        v_bd = vector_normalize(d.vector(b))
        v_cd = vector_normalize(d.vector(c))
        v_d = vector_add(v_bd, v_cd)
    elif num == 1:
        v_ad = vector_normalize(d.vector(a))
        v_cd = vector_normalize(d.vector(c))
        v_d = vector_add(v_ad, v_cd)
    elif num == 2:
        v_ad = vector_normalize(d.vector(a))
        v_bd = vector_normalize(d.vector(b))
        v_d = vector_add(v_ad, v_bd)
    #----------start of the transformation----------
    new_a = a.move_by(v_a)
    new_b = b.move_by(v_b)
    new_c = c.move_by(v_c)
    new_d = d.move_by(v_d)
    #----------end of the transformation----------
    print("after transformation")
    print(f"a = {a.show()}, b = {b.show()}, c = {c.show()}, d = {d.show()}")
        
    
if __name__ == '__main__':
    main()
