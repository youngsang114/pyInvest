# Chapter 03-02
# Special method(Magic Mehtod)
# 파이썬의 핵심 -> 1.시퀀스(sequence) 2.반복(Iterator), 3.함수(Functions), 4.클래스(Class)
# 클래스 안에 정의할 수 있는 특정한(Built- in : 이미 만들어진) 메서드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id,type -> value

# 일반적인 튜플

pt1 = (1.0,5.0)
pt2 = (2.5,1.5)
# 이것만 보면 어떤 데이턴지 알기가 어렵다! 

from math import sqrt

l_leng1 = sqrt((pt1[0]-pt2[0])**2 +(pt1[1]-pt2[1])**2)
print(l_leng1)

# Named tuple을 사용해서 데이터를 구해보자

from collections import namedtuple

# 네임드 튜플 선언

Point = namedtuple('Point','x y')

pt3 = Point(1.0,5.0)
pt4 = Point(2.5,1.5)

print(pt3,pt4)

l_leng2 = sqrt((pt3.x-pt4.x)**2 +(pt3.y-pt4.y)**2)
print(l_leng2)

### NamedTuple 선언 방법 ###

Point1 = namedtuple("Point", ['x','y'])
Point2 = namedtuple("Point", 'x,y')
Point3 = namedtuple("Point", 'x y')
Point4 = namedtuple("Point", 'x y x class',rename=True) # default = False


# Dict to Unpacking

temp_dict = {'x':75, 'y':55}

## unpacking

unpackingP3=Point3(**temp_dict)
print(unpackingP3)


print()

# 출력
print(type(Point4))
print(Point1,Point2,Point3,Point4)

p1 = Point1(x =10,y=35)
p2 = Point2(20,40)
p3 = Point3(45,y=20)
p4 = Point4(10,20,30,40)

print()

print(p1)
print(p2)
print(p3)
print(p4) # rename이 false이면 만들어지지 않는다! class가 예약어이기 때문에! : rename test


## 사용
print(p1.x + p2.y)

# unpacking
x,y =p2
print(x,y)

## 네임드 튜플의 메서드

temp = [52,37]

# _make() : 리스트를 네임드 튜플 객체를만들어주는 메서드 
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인

print(p1._fields,p2._fields,p3._fields,p4._fields)

# _asdict() : OrderedDict 반환

print(p1._asdict())
print(p4._asdict())

# 실 사용 실습
# 반 20 명 , 4개의 반 (A,B,C,D)


Classes = namedtuple('Classes', ['rank','number'])

# 그룹 리스트 선언

numbers= [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

# List Comprehension

studetns = [Classes(rank,number) for rank in ranks for number in numbers]

print(len(studetns))
print(studetns)

# 추천

studetns2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1,21)]]

print(len(studetns2))
print(studetns2)