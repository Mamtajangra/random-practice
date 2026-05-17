x = 0.1 + 0.1 + 0.1
print(x)
#  to solve this we will import decimal 0.30000000000000004 to reduce this result
import math
from decimal import Decimal
x = Decimal("0.1") + Decimal("0.1")+ Decimal("0.1")
print(x)
y = Decimal("0.1") + Decimal("0.1")+ Decimal("0.1") - Decimal("0.1")
print(y)
from fractions import Fraction
z = Fraction(2,5)
print(z)