#  Chapter 04-01
# 시퀀스 형
# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형 [list,tuple,collections.deque])
# 플랫(Flat : 한개의 자료형[str,bytes,bytearray, array.array, memoryview])
# 가변(list,bytearray,array.array,memoryview,deque)
# 불변(tuple,str,bytes)

# [해시 테이블] : Key에 Value를 저장하는 구조
# 파이썬  dict :  해쉬 테이블 -> 예 232324234235
# 키값의 연산 결과에 따라 직접 접근이 가능한 구조
# key값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조!

# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인 -> 고유하다

t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])

print(hash(t1))
# print(hash(t2)) # list는 수정이 가능하기 때문에, hash 함수를 사용할 수 없다
# 즉 hash함수는 불변한 값에 대해서만 사용할 수 있다

print()
print()

# Dict [Setdefault] 예제
source = (('k1','val1'),
          ('k1','val2'),
          ('k2','val3'),
          ('k2','val4'),
          ('k2','val5'))

new_dict1 = {}
new_dict2 = {}

# No Use Setdefault

for k,v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault

for k,v in source:
    new_dict2.setdefault(k,[]).append(v)
print(new_dict2)

# 주의 -> 덮어써버림!!!
new_dict3 = {k : v for k,v in source}
print(new_dict3)
