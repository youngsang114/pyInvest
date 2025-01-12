### 데코레이터(Decorator)

# 데코레이터를 이해하기 위해서는 다음을 잘 이해해야 한다.
# 1. 클로저
# 2. 함수를 일금 인자로 활용하는 방법
# 3. 가변 인자
# 4. 인자 풀기(unpacking)
# 5. 파이선 소스코드를 불러오는 자세한 과정


# 데코레이터 장점
# 1. 장점, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 함수
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 디버깅 감소


# 데코레이터 실습

import time

def perf_clock(func):

    def perf_clocked(*args):
        # 함수시작시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
    
        # 함수 종료 시간
        et = time.perf_counter()
        # 실행 함수명
        name  = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결촤 룰력
        print('[%0.5fs] %s(%s) -> %r' %(et-st,name,arg_str,result))
        return result
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용

none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
print()
none_deco2(100,200,300,400,500)


print()
print()
# 데코레이터 사용
@perf_clock
def time_func(seconds):
    time.sleep(seconds)
@perf_clock
def sum_func(*numbers):
    return sum(numbers)

print('-' * 40, 'Called Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called Decorator -> sum_func')
print()
none_deco2(100,200,300,400,500)