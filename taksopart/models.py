


class AbstactAccount:
    
    def __init__(self,**kwargs) -> None:
        self.name = kwargs['name']
        self.last_name  = kwargs['last_name']
        self.age = kwargs['age']
        self.gender = kwargs['gender']

    def __str__(self) -> str:
        return str(self.__dict__)

class DriverAccount(AbstactAccount):
    def __init__(self, **kwargs) -> None:
        self.rating = kwargs['rating']
        self.age_of_work = kwargs['age_of_work']
        super().__init__(**kwargs)

class UserAccount(AbstactAccount):
    def __init__(self, **kwargs) -> None:
        self.balance = kwargs['balance']
        self.bonuses = kwargs['bonuses']
        super().__init__(**kwargs)

class Car:
    
    def __init__(
        self,
        mark:str,
        model:str,
        milliage:int,
        color:str,
        driver:DriverAccount,
    ) -> None:
        self.mark = mark
        self.model = model
        self.milliage = milliage
        self.color = color
        self.driver = driver
        self.is_busy = False
    
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)

class TaksoPark:
    def __init__(
        self,
        car_list,
        user_list,
        ) -> None:
        self.car_list = car_list
        self.user_list = user_list
        self.driver_list = [car.driver for car in car_list]

    def __str__(self) -> str:
        return str(self.__dict__)