x = int(input("enter the year:"))
if (x % 400 == 0) or (x%4 ==0 and x%100 !=0):
    print("leap")
else:
    print("not leap")    