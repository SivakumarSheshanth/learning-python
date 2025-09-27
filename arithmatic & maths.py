#friend = 5

#friend= friend+1
#friend += 1
#friend=friend-1
#friend-=1
#friend = friend *2
#friend *= 2
#friend = friend / 2
#friend /= 2
#friend = friend ** 3
#friend **= 3
#friend =friend % 2
#friend %=2

#print(friend)

#x= 3.11
#y= -4
#z=5

#result = round(x)
#result = pow(y,2)
#result = abs(y)
#result = max(x, y, z)
#result = min(x, y, z)

#print(result)

import math

#x= 9.9
#print (math.pi)
#print (math.e)
#result= math.sqrt(x)
#result= math.ceil(x)
#result= math.floor(x)
#print(result)

#exercise1
import math

radius=float(input("enter a radius:"))
circumfernce=2*math.pi* radius
print (f'the circumference of the circle is {round(circumfernce)}cm')

#exercise2
import math

radius= float(input("enter the radius:"))
area= math.pi*pow(radius,2)
print(f"the area of the circle {round(area)}cm^2")

import math

a=float(input("enter the side a:"))
b=float(input("enter the side b:"))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"side c  is {round(c)}")
