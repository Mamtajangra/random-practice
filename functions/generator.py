def generator():
    print("hello")
    yield 1
    print("ram")
    yield 2
    print("honey")
    yield 3

    print("end")
g= generator()
next(g)
next(g)
