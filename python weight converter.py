#python weight converter

weight=float(input("enter the weight: "))
unit=input("enter the unit (K or L): ")
if unit =="K":
    weight= weight * 2.205
    unit="kg."
elif unit =="L":
    weight=weight/2.205
    unit="lbs."

else:
    print(f"{unit} is not a valid unit")
print(f"ur weight is {weight} {unit}")