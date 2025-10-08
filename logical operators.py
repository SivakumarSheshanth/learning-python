#logical operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be true
#                    and = both condition must be true
#                    not = inverts the condition(not false, not true)

#or condition
temp=-5
is_raining= True

if temp>=34 or temp<=0 or is_raining:
    print("the program is canceled")
else:
    print("the program will continue")

#and & not condition
temp=286
is_sunny= False

if temp>38 and is_sunny:
    print("its very sunny today")
    print("its hot today")
elif temp<0 and is_sunny:
    print("its very cold tdy")
elif temp<=38 and temp>=0 and is_sunny:
    print("its warm today")
    print("its very sunny today")
elif temp>38 and not is_sunny:
    print("its very cloudy today")
    print("its hot today")
elif temp<0 and not is_sunny:
    print("its very cloudy tdy")
elif temp<=38 and temp>=0 and not is_sunny:
    print("its cloudy today")
    print("its very cloudy today")
