class Car():
    """
    Car class
    Author : Yoo
    Date : 2025.01.11
    Description : Class,Static, Instance Method
    """

    ## 클래스 변수는 모든 인스턴스가 공유한다!!!
    price_per_raise = 1.0 # 관세

    def __init__(self,company,details):
        self._company = company # protect 접근 제어자!!!
        self._details = details
        
    def __str__(self): ## 사용자 레벨
        return 'str : {} - {}'.format(self.company,self.details)
    
    def __repr__(self): ## 개발자 레벨
        return 'repr : {} - {}'.format(self.company,self.details)
    
    # Instance Method
    # Self : 객체의 고유한 속성값을 사용한다
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {}, {}'.format(self._company,self._details.get('price')))
    
    # Instance Method
    def get_price(self):
        return "Before Car Price -> company : {}, price : {}".format(self._company,self._details.get('price'))
    
    # Instance Method
    def get_price_culc(self):
        return "After Car Price -> company : {}, price : {}".format(self._company,self._details.get('price') * Car.price_per_raise)
    
    # Class Method -> 1. 캡슐화 가능, 2.필요한 로직도 추가할 수 있다
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print("Succeed! price increased.")
    
    # Static method -> 파라미터가 없다. 좀더 유연
    @staticmethod
    def is_bmw(instance):
        if instance._company == 'Bmw':
            return 'OK! This car is {}'.format(instance._company)
        return 'sorry this car is not Bmw!'

    

# Self 의미 : 인스턴스에서 첫번째 매개 변수가 self이다.

car1 = Car('Ferrari',{'color' : 'white', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw',{'color' : 'black', 'horsepower' : 200, 'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

#가격 정보(직접 접근 -> 지양)
print(car1._details.get('price')) # 캡슐화에 위배되는 코드!!! -> 보통은 메서드를 만들어서 필요한 것만 반환하는 방법을 사용한다.!!!

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격정보(인상 후)
Car.price_per_raise = 1.4 # 지양할 필요가 있다!!!

print(car1.get_price_culc())
print(car2.get_price_culc())

# 클래스 메서드 확인
Car.raise_price(0.8)
Car.raise_price(1.8)

# 인스턴스로 호출(static)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출(static)
print(Car.is_bmw(car2))
