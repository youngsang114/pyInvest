#  Chapter 04-01
# 시퀀스 형
# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형 [list,tuple,collections.deque])
# 플랫(Flat : 한개의 자료형[str,bytes,bytearray, array.array, memoryview])
# 가변(list,bytearray,array.array,memoryview,deque)
# 불변(tuple,str,bytes)

# 지능형 리스트(Comprehending Lists)
chars = '+)_!@#!~$@#!'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending List + Map, Filter
# 40 이상의 유니코드 리스트만 가져오기

code_list2 = [ord(x) for x in chars if ord(x)>=40]
print(code_list2)

code_list3 = list(filter(lambda x : x>=40, [ord(x) for x in chars]))
print(code_list3)

code_list4 = list(filter(lambda x : x>=40, map(ord,chars)))
print(code_list4)

print([chr(s) for s in code_list4])


# Generator 생성자

import array 

# Generator : 한번에 한개의 항목을 생성(메모리 유지 X)
# ()안에 감싸준다
# 아직 생성하지 않고, 첫 번째 값 반환을 준비한 상태

tuple_g = (ord(s) for s in chars)
print(tuple_g)
print(type(tuple_g))

print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print()

array_g = array.array('I', (ord(s) for s in chars)) # array 첫 번째 인자 = 타입코드 (I : 부호 없는 정수 의미)

print(array_g)
print(array_g.tolist())

# 제네레이터 예제

print(('%s' %c + str(n) for c in ['A','B','C','D'] for n in range(1,21)))

for s in ('%s' %c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)

print()
print()

# 리스트 주의 (깉은, 얕은)

marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] *4
print(marks1)

# 수정

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명

print([id(x) for x in marks1])
print([id(x) for x in marks2])
