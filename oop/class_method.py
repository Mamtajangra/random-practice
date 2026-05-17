class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model = model
    def car_search(self):
        return f"the name of the brand of the car is {self.brand} and the model is {self.model}"


c1 = Car("mahindra","scorpio")
c2 = Car("tata","safari")  
print(c2.model,c1.brand)
print(c1.car_search())