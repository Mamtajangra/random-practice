# def decorator(func):
#     def wrapper (*arg,**kwargs):
#         print("start")
#         func()
#         print("end")
#     return wrapper 
   
    


# @decorator
# def sum():
#     print("hello")
# sum()


import time 

def timer(func):
    def wrapper(*args,**kwargs):

        start = time.time()
        print("firstly say")
        func(*args,**kwargs)
        end = time.time()
        print("end - start")
    return wrapper    
@timer
def example(n):
    time.sleep(n)

example(2)    




    