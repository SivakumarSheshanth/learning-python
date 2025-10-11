#while loop = execute some code WHILE some condition remains true

#name= input("What is your name? ")
#while name=='':
#    print("u didn't enter ur name")
#    name = input("What is your name?")
#print(f"hello {name}")

#age= int(input("How old are you?"))
#while age < 0:
#    print("age can't be nagative")
#    age = int(input("How old are you?"))
#print(f"u r {age}")

#food= input("What food do you want to buy?(q to quit) ")
#while not food == "q":
#    print(f'u like {food}')
#    food= input("Whats the second food do you want to buy?(q to quit) ")
#print("bye")

num=int(input("Enter a number between 1 and 10: "))
while num<1 or num>10:
    print("Enter a valid number between 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))
print(f'ur number is {num}')