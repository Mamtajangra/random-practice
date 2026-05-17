# username = "jojo"
# def func1():
#     username = "koko"
#     print(username)
# print(username)
# func1()




# username = 7
# def func2(m):
#     res = username + m
#     return res
    
# final = func2(9)

# print(final)


x = 25

def func3():
    x = 78

    def func4():
        print(x)
    return func4()

func3()