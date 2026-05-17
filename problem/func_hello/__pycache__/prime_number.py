x = int(input("enter nubers:"))
is_prime = True
if x >1:

    for i in range(2,x):
        if x % i == 0:
            is_prime = False
            break

        # print("no prime")
    
print(is_prime)