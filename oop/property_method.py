class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model
    def detail(self):
        return f" the name is {self.brand} and model is {self.__model}"
    @staticmethod
    def colour():
        return"the colour of the car is blck"
    @property
    def model(self):
        return self.__model
    
    


c1 = Car("mahindra","scorpio")
c2 = Car("toyota","nexon")
# c2.model = "city"
print(c1.detail())
print(c2.model)
print(c1.model)  
print(Car.colour())      


# main ek aisa method create karu ki sab usko access nhi akr paaye but mere method ki wjeh se kar le and hmm value ko bhi update nhi kr sakte
'''property method hota hia ki hmko kisis ek attribute ko read only krna hai means ki private but access kr ske jisko '''