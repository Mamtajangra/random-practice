y =input("enter the value:")
x = len(y)
if x <6:
    print("weak password")
elif x> 6 and x<= 10:
    print("medium password")
else:
    print("strong password")        