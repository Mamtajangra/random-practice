pet = input("enter the pet:")
age = int(input("enter the value:"))
if pet == "dog":
    if age < 2:
        print("puppy food")
elif pet == "cat":
    if age > 5:
        print("senior cat food") 

else:
    print("unknown pet")               