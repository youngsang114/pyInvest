#  Chapter 04-01

# [해시 테이블] : Key에 Value를 저장하는 구조 -> 적은 리소스로 많은 데이터를 효율적으로 관리
# 파이썬  dict :  해쉬 테이블 -> 예 232324234235
# 키값의 연산 결과에 따라 직접 접근이 가능한 구조
# key값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조!


## Dict 및 Set 심화

# Immutable Dict

from types import MappingProxyType

d = {'key1':'value1'}

# Read Only
# 변수명에서 frozen을 붙여 수정 X하게 알리기
d_frozen = MappingProxyType(d)

print(d,id(d))
print(d_frozen,id(d_frozen))

# 수정 가능
d['key2'] = 'value2'

# 수정 불가능
# d_frozen['key2'] = 'value2'


print()
print()


s1 = {'Applie', 'Orange', 'Orange', 'kiwi','kiwi'}
s2 = set(['Applie', 'Orange', 'Orange', 'kiwi','kiwi'])
s3 = {3}
s4 = {} # 이건 딕셔너리
print(type(s4))

s5 = frozenset({'Applie', 'Orange', 'Orange', 'kiwi','kiwi'})
s1.add('Melon')
print(s1)

# 추가 불가
# s5.add('Melon')

print(s1,type(s1))
print(s1,type(s2))
print(s1,type(s3))
print(s1,type(s4))
print(s1,type(s5))


# 선언 최적화
# 파이트 코드 -> 파이썬 인터프리터 실행
from dis import dis
print('--------')
print(dis('{10}'))
print('--------')
print(dis('set([10])'))