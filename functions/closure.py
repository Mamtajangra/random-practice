'''function ke end hone ke baad bhi kuch variables destroy nhi hote internal function inka reference rkh leta hai and ye useful hote hai usme
'''
def clos_ure():
    x = 23
    def clos_ure2():
        print(x)
    return clos_ure2() 
f = clos_ure()
print(f)

'''according to rule after the end of 1st function x should be destroyed but it gives value whenever i print it on 2nd function
its called closure .....it used in encapsulation and decorator
Closure is like carrying a backpack of remembered variables.'''