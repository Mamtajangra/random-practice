def kwarg(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

kwarg(name ="radha",age = 13,location="mumbai")
kwarg(age = 78)