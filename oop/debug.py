def debug(func):
    def wrapper(*args,**kwargs):
        
        arg_val = " ,".join(str(args) for arg in args)
        kwarg_val = " ,".join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling:{func.__name__}with {arg_val} and {kwarg_val}")
        return  func(*args,**kwargs)
    return wrapper







@debug
def greet(name,greeting = "hiii"):
    print(f"say {name} {greeting}")        


greet("mamu","hii")



#  :{func.__name__}w this determne the name of the function ,decorator ka mtlb h origina function ko decorate krke bhejna aur 
# important hai kyunki ek baaar set krdo decorator fir sara function whi se pass hoke jaayega and after this 
# wrapper = add extra code 
# debug = ye decorator h kuch bhi name ho skta hia
# func= original function hai isko decorate krna hai 
