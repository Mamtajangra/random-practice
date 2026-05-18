def decorator(func):
    def wrapper(*args,**kwargs):
        print("before")
        func()
        print("after")
    return wrapper    





@decorator
def greet():
    print("hello mamu")

greet()    