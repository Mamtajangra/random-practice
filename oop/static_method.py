class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def detail(self):
        return f"the brand name is {self.brand} and model name is {self.model}"
    @staticmethod
    def fuel_type():
        return"all veehicle required fuel"


c1 = Car("mahindra","scorpio")
c2 = Car("toyota","nexon")
print(c1.detail()) 
print(Car.fuel_type())   


# this method dont depend on class and instance no requirement of self here 
# ye decorator ke roop main kaam krta h object isko call bhi nhi kr skti
# class isko access klr skti h but object nhi like car.fuel likha hmne