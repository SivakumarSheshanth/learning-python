unit= input("is the tempreature in celcius or fahrenheit? (C/F): ")
temp= int(input("whats the tempreture? "))

if unit =="C":
    temp= (temp*9/5)+32
    print(f"the tempreture in fahrenheit is {temp}")
elif unit=="F":
    temp=round((temp-32)*5/9)
    print(f"the tempreture in celcius is {temp}")
else:
    print("invalid unit")