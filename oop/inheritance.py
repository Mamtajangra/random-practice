class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def car_detail(self):
        return f" the name of the brand is {self.brand} and its model is {self.model} "
    
class Electriccar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 

    def car_detail2(self):
        return f" the name of the brand is {self.brand} and its model is {self.model} and its battery_size is {self.battery_size}"       

c1 = Car("Toyota","corolla")
c2 = Car("mahindra","scorpio")
print(c2.car_detail())  

c_new = Electriccar("tesla","modelS","80kwh")


print(c_new.car_detail2())