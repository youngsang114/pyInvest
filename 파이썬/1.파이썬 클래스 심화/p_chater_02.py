
class Car():
    """
    Car class
    Author : Yoo
    Date : 2025.01.11
    """

    ## 클래스 변수는 모든 인스턴스가 공유한다!!!
    car_count = 0

    def __init__(self,company,details):
        self._company = company # protect 접근 제어자!!!
        self._details = details
        Car.car_count +=1
        
    def __str__(self): ## 사용자 레벨
        return 'str : {} - {}'.format(self.company,self.details)
    
    def __repr__(self): ## 개발자 레벨
        return 'repr : {} - {}'.format(self.company,self.details)
    
    def __del__(self):
        Car.car_count -=1
        

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {}, {}'.format(self._company,self._details.get('price')))

# Self 의미 : 인스턴스에서 첫번째 매개 변수가 self이다.

car1 = Car('Ferrari',{'color' : 'white', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw',{'color' : 'black', 'horsepower' : 200, 'price' : 6000})
car3 = Car('Audi', {'color' : 'silver', 'horsepower' : 100, 'price' : 4000})    

print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company ==car2._company)
print(car1 is car2)

# dir & __dict__
# dir : 해당 인스턴스가 가지고 있는 모든 속성들들 list로 보여주는 것
print(dir(car1))
print(dir(car2))

print()
print()
# __dict__ : 딕셔너리로, 해당 인스턴스가 가지고 있는 key,value값들을 보여주는 것
print(car1.__dict__)
print(car2.__dict__)


# Doctring
# 사용 방법을 보여준다 -> 원칙적으로 함 !

print(car1.__doc__)


# 실행
car1.detail_info()

# 에러
Car.detail_info(car2) # 명시적으로 car2의 정보를 self로 넣어줘서 출력!

# 클래스 변수의 공유 확인
print(car3.__dict__)
print(car3.car_count)
print(dir(car1))

del(car2)
#삭제 확인
print(car3.__dict__)
print(car3.car_count)

# 인스턴스 네인스페이스에서 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 변수 검색 후 -> 상위(클래스 변수, 부모클래스 변수) 검색!)