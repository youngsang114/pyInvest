#  Chapter 04-01
# 시퀀스 형
# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형 [list,tuple,collections.deque])
# 플랫(Flat : 한개의 자료형[str,bytes,bytearray, array.array, memoryview])
# 가변(list,bytearray,array.array,memoryview,deque)
# 불변(tuple,str,bytes)

# Tuple Advanced
# Unpacking
# a,b =b,a

print(divmod(100,9))
print(divmod(*(100,9))) # 튜플을 unpacking 해서 2개의 인자로 divmod함수에 넣어줌
print(*(divmod(100,9)))

print()

x,y,*rest = range(10)
print(x,y,rest)

x,y,*rest = range(2)
print(x,y,rest)

x,y,*rest = 1,2,3,4,5
print(x,y,rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15,20,25)
m = [15,20,25]

print(l,id(l))
print(m,id(m))

l = l *2
m = m*2

print(l,id(l))
print(m,id(m))

l *=2
m *=2

print(l,id(l))
print(m,id(m))

print()
print()

# sorted vs sort
# reverse, key = len, key = str.lower, key = func...

# sorted : 정렬 후 새로운 객체 변환
f_list = ['orange','apple','mange','lemon','coconut']

print(f_list)
print('sorted - ',sorted(f_list))
print('sorted - ',sorted(f_list, reverse=True))
print('sorted - ',sorted(f_list, key=len)) # 글자수 기준으로 정렬
print('sorted - ',sorted(f_list,key= lambda x : x[-1]))
print('sorted - ',sorted(f_list,key= lambda x : x[-1], reverse=True))

# sort : 정렬 후 객체 직접 변경

print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key = len), f_list)
print('sort - ', f_list.sort(key=lambda x :x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x :x[-1], reverse=True), f_list)


# List VS Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : ndarray, 같은 숫자 기반에서 사용!(성능), AI, Vector -> 고속의 연산, 배열(리스트와 거의 호환)