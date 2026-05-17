import math
def multi_values(r):
    area = math.pi*r*r
    circum = 2*math.pi*r
    return[area,circum]
res= multi_values(4)
print(res)