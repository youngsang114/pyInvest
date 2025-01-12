# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(Scope)

# Ex1
def func_v1(a):
    print(a)
    # print(b)

# Ex2
b = 20
def func_v2(a):
    print(a)
    print(b)

func_v2(10)


# Ex3
c=30
def func_v3(a):
    print(a)
    c=40
    print(c)
    

func_v3(10)

# Ex4
c=30

def func_v3(a):
    global c # 이 시점에서 전역변수 c를 참조!
    print(a)
    print(c)
    c=40 # 전역변수 c의 값을 30에서 40으로 치환
    
print('>>',c)
func_v3(10)
print('>>>',c)


### python Clousure(클로저) 사용 이유
# scope가 닫혀도, 생성됐던 변수를 소멸하지 않고 기억하는 역할
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착 상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되, 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 쿨로저는 불변자료구조 및 atom(원자성), STM -> 멀티스레드 프로그래밍에 강점


a = 100

print(a+1000,a+100)

# 결과 누적(함수 사용)
print(sum(range(1,6)))
print(sum(range(7,11)))

# 클래스 이용

class Averager():

    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series , len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성

averager_cls = Averager()
print(dir(averager_cls))

# 누적
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))