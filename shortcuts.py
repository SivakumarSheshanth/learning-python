
#name= (input("Enter your name : "))
#phone_number= (input("Enter your phone number : "))
#result=len(name)
#result=name.find("f")
#result=name.rfind("r")
#name= name.capitalize()
#name = name.upper()
#name =name.lower()
#result=name.isdigit()
#result=name.isalpha()
#result=phone_number.count("4")
#phone_number=phone_number.replace("-"," ")

#print(phone_number)
#print(help(str))

#exercise
#validate user input exercise
#username is no more than 12 characters
#username must not contain spaces
#username must not contain digits

username=input("enter your username: ")
if len(username)>12:
    print ("username too long")
elif not username.find(" ")==-1:
    print("invalid username")
elif not username.isalpha():
    print("username valid")
else:
    print(f"welcome {username}")
