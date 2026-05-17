# encapsulation with the help of get method


# class Car:
#     def __init__(self,brand,model):
#         self.__brand= brand
#         self.model = model
#     def get_brand(self):
#         return self.__brand  
#     def car_search(self):
#         return f"the name of the brand of the car is {self.__brand} and the model is {self.model}"


# c1 = Car("mahindra","scorpio")
# c2 = Car("tata","safari")  
# print(c2.model,c1.__brand)
# print(c1.car_search())


'''getter method helps to make brand private it is accissible only in class but not when we create any object it became private here
we hide it with the help of double underscore '''


# ###############################
class Animal:
    def __init__(self,name,legs):
        self.__name = name 
        self.legs = legs
    def animal_detail(self):
        return f"the name of the animal is {self.__name} and its legs are{ self.legs}"
    def get_name(self):
        return self.__name 
class Sound(Animal):
    def __init__(self,name,legs,colour):
        super().__init__(name,legs) 
        self.colour = colour   
    

a1 = Animal("dog",4)
a2 = Animal("kangaaroo",2)
a3 = Sound("dog",4,"black")
print(a1.name)
print(a3.name)
print(a2.animal_detail())
print(a1.get_name())    
        