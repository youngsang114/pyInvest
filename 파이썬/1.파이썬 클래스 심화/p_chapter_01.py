# 차량 1

car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'white'},
    {'horsepower' : 400},
    {'price' : 8000}
]

# 차량 2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color' : 'black'},
    {'horsepower' : 200},
    {'price' : 6000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'silver'},
    {'horsepower' : 100},
    {'price' : 4000}
]

# 리스트 구조
# 관리하기 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편 -> 유지보수 불편
car_company_list = ['ferrari','bmw','audi']
car_detail_list = [
    {'color' : 'white', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'black', 'horsepower' : 200, 'price' : 6000},
    {'color' : 'silver', 'horsepower' : 100, 'price' : 4000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키) -> 예외 처리 등
car_dict = [
    {'car_company' : 'Ferrari', 'car_detail' :  {'color' : 'white', 'horsepower' : 400, 'price' : 8000}},
    {'car_company' : 'bmw', 'car_detail' :  {'color' : 'black', 'horsepower' : 200, 'price' : 6000}},
    {'car_company' : 'audi', 'car_detail' :  {'color' : 'silver', 'horsepower' : 100, 'price' : 4000}}
]

del car_dict[1]
print(car_dict)

## 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self,company,details):
        self.company = company
        self.details = details
    def __str__(self): ## 사용자 레벨
        return 'str : {} - {}'.format(self.company,self.details)
    def __repr__(self): ## 개발자 레벨
        return 'repr : {} - {}'.format(self.company,self.details)


car1 = Car('Ferrari',{'color' : 'white', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw',{'color' : 'black', 'horsepower' : 200, 'price' : 6000})
car3 = Car('Audi', {'color' : 'silver', 'horsepower' : 100, 'price' : 4000})
print(car1)
print(car2)
print(car3)
    
print(car1.__dict__) ## 딕셔너리 상태로 인스턴스의 속성 정보를 볼 수 있다.
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1)) # car1의 모든 메타 정보를 보여준다


# 리스트로 인스턴스 관리

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print('----------')


print(car1)

# 반복문에서는 __repr__로 출력, 명시적으로 출력 가능능
for x in car_list:
    # print(repr(x))
    # print()
    print(x)