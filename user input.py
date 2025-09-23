

#Input() = A function that prompts the user to enter data
#          Return the entered data as a string

#want put f str if variable used

name = input("what is ur name? :")
age =int(input ("whats ur age?: "))

age = int(age)
age = age + 1
print(f"hello {name}")
print("happy birthday")
print(f"alright ur {age}")

#exercise 1 Rectangle area calc

length = int(input("length of the rectangle?:"))
width = int(input("width of the rectangle?:"))

area = length * width
print(f"area is {area}")

#exercise 2 Shopping cart program

item= input("what item do u want to buy: ")
price= float(input("whats the price of the item?:"))
quantity = int(input("whats the quantity of the item?:"))


total = price *quantity
print(f"u bought {item} x {quantity}/s")
print(f" u hv bought items for {total}")