class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def consum(self):
        return "petrol or diesel"
class Electriccar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def consum(self):
        return "electric charge"


c1 = Car("toyota","corolla")
c2 =  Electriccar("tesla","modelS","80kwh")
print(c1.consum())
print(c2.consum())       
