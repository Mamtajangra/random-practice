def fact(n):
    if n== 0:
        return 1
    else:
        res= n*fact(n-1)
    return res
    # num = num -1
print(fact(5))

