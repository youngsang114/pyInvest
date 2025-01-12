# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''
    if n ==1:
        return 1
    return n*factorial(n-1)


class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial)) ## class 'function' -> 일급 객체 취급
print(type(A))
print(dir(factorial)) # 함수지만 객체취급 ! (__lt__,__repr__)
print()
print(set(dir(factorial)) - set(dir(A))) # 함수와 클래스의 교집합을 빼, 함수만 가지고 있는 속성들만 나옴
print(factorial.__name__)
print(factorial.__code__)

print()
print()

## 1. 변수에 할당 가능

var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1,11))))

## 2. 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce

print(list(map(var_func, filter(lambda x : x%2, range(1,6))))) # lambda의 익명함수를 filter의 인수로 넣어줄 수 있다.
print([var_func(i) for i in range(1,6) if i %2 !=0 ]) 

# reduce

from functools import reduce
from operator import add

print(reduce(add,range(1,11)))
print(sum(range(1,11)))

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수를 작성해라!
# 일반 함수 형태로 리팩터링을 권장한다

print(reduce(lambda x,y : x+y, range(1,11)))

# Callable : 호출 연산자 -> 메서드 형태로 호출 가능한지 확인
# 호출 가능한지 확인 (__callable__)

print(callable(str), callable(A),callable(list), callable(var_func), callable(factorial),callable(3.14))

print(str('a'))


## partail 사용법 : 인수를 고정 -> 콜백 함수 사용시!
from operator import mul
from functools import partial

print(mul(10,10))
# 인수를 항상 고정하고 싶음! (한쪽을 항상 고정!!)

five = partial(mul,5) # mul즉 함수는 일급객체므로 partial의 인수로 들어갈 수 있다

# 고정 추가
six = partial(five,6)
print(five(5))
print(six())
print([five(i) for i in range(1,11)])