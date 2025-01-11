# Chapter 03-02
# Special method(Magic Mehtod)
# 파이썬의 핵심 -> 1.시퀀스(sequence) 2.반복(Iterator), 3.함수(Functions), 4.클래스(Class)
# 클래스 안에 정의할 수 있는 특정한(Built- in : 이미 만들어진) 메서드


# [클래스 예제 2]
# 벡터(x,y) -> 크기와 방향을 갖음


import math

class Vector(object):
    def __init__(self,*args): # *args : 패킹
        '''
        Create a vector, example : v = Vector(5,10)
        '''
        if len(args) == 0:
            self._x , self._y = 0,0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the Vector informations.'''
        return 'Vector({},{}).'.format(self._x,self._y)
    
    def __add__(self,other):
        '''Reutrn the vector addition of self and other'''
        return Vector(self._x+other._x, self._y+other._y)
    
    def __mul__(self,y):
        return Vector(self._x*y, self._y*y)
    
    def __bool__(self):
        return bool(max(self._x,self._y))
    
    def dis(self,other):
        return math.sqrt(math.pow(self._x - other._x ,2) + math.pow(self._y - other._y, 2))



# Vector 인스턴스 생성

v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직메서드 발생
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1+v2)
print(v1*5)
print(bool(v1))
print(bool(v3))
print(v1.dis(v3))