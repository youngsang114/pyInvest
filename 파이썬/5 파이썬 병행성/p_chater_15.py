# 병행성(Concurrency)
# iterator, generator

# 파이썬 반복 가능한 타입
# collections, text file, list, dict , set , tuple, unpacking *args... : iterable하다

# 반복 가능한 이유? -> 내부적으로 iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOP'

print(dir(t))
for c in t:
    # print(c)
    pass

w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()


# 반복형 확인

from collections import abc
print(dir(t))
print(hasattr(t, '__iter__')) # hasstr :  그 속성을 가지고 있니?
print(isinstance(t, abc.Iterable))

# next()


class WordSplitter():

    def __init__(self,text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word  = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx +=1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' %(self._text)
    

wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))


print()
print()

# Generator 패턴

# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양이 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator():
    def __init__(self,text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return
    def __repr__(self):
        return 'WordSplitGenerator(%s)' %(self._text)

wg = WordSplitter('Do today what you could do tomorrow')

wt = iter(wg)
print(wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

print()
print()