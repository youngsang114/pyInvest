# Chapter 03-02
# Special method(Magic Mehtod)
# 파이썬의 핵심 -> 1.시퀀스(sequence) 2.반복(Iterator), 3.함수(Functions), 4.클래스(Class)
# 클래스 안에 정의할 수 있는 특정한(Built- in : 이미 만들어진) 메서드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10
print(type(n))
print(n+100) # [내부적]으로 만들어진 __add__ 함수가 실행된 것!!!
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))


print()
print()


# [클래스 예제1]

class Fruit():
    def __init__(self,name,price):

        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit name : {} , price : {}'.format(self._name,self._price)
    
    def __add__(self,x):
        print('Called >> __add__')
        return (self._price + x._price)
    
    def __sub__(self,x):
        print('Called >> __sub__')
        return (self._price - x._price)
    
    def __le__(self,x):
        print('Called >> __le__')

        if self._price <= x._price:
            return True
        else:
            return False
    
    def __ge__(self,x):
        print('Called >> __sub__')
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Orange', 7000)
s2 = Fruit('Banana',3000)


# 매직메소드드
print(s1+s2)
print(s1-s2)
print(s1>=s2)
print(s1<=s2)