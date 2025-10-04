# if = do some code only if some condition is True
#       else do something else

age=int(input("Enter your age: "))
if age>=100:
    print ("u r too old to sign up")
elif age >=18:
    print("u r signed up")
elif age<=0:
    print(" u havn't born yet")

else:
    print("u must ne 18+ to signed up")



#example 2

response=(input(f"do u like the food? (Y/N):"))
if response =="Y":
    print("thank u for ur feedback")
elif response == "y":
        print("thank u for ur feedback")
else:
    print("we r sorry for that")


#example 2

name=(input("enter ur name: "))

if name=="":
    print("u haven't type anything")
else:
    print(f"welcome {name}")

#example 3 boolean

for_sale = False
if for_sale:
    print("this item is for sale")
else:
    print("this item is not for sale")