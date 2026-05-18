# hme ek decorator create krna hai ki jisme wo value ko store karke rakhe 
import time

def cache(func):
    def wrapper(*args):
        cache_val = {}
        if args in cache_val:
            return cache_val[args]
        
        
        res = func(*args)
        cache_val[args] = res
        return res
    return wrapper

@cache
def sum(a,b):
    time.sleep(4)
    return a+b


print(sum(2,5))
print(sum(8,5))