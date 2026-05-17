class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
class Battery:
    def battery_info(self):
        return"this is battery"
class Engine:
    def engine_info(self):
        return"this is engine"
class Electriccar(Car,Engine,Battery):
    def __init__(self,brand,model,fuel):
        super().__init__(brand,model)
        self.fuel = fuel    

new_car = Electriccar("tesla","model s","8-kwh")
print(new_car.engine_info())     
print(new_car.battery_info())   
         


        #  electric car is inherit from engine battery and car like multiple inheritance possible in class