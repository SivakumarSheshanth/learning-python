#conditional expressions = A one line shortcut for if-else statement(ternary operator)
#                          print or assign one or two values based on condition
#     formula              X if condition else Y

num=0
a=5
b=4
age=139
user= "admin"

#print("positive"if num>0 else "negative")
#print("even"if num%2==0 else "odd")

#max_num = a if a>b else b
#min_num = a if a<b else b
#print(max_num)
#print(min_num)

#status= "adult" if age>=18 else "child"
#print(status)
access_level= "full access" if user=="admin" else " not allowed"

print(access_level)
