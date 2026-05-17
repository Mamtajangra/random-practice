age = int(input("enter the age of person:"))
if age < 13:
    print("child")
elif age >=13 and age <= 19:
    print("teenager")
elif age >=20 and age <= 59:
    print("adult")
elif age >50:
    print("senior")             