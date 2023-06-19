for num in range(1,2,1):
    age = int(input("enter age="))
    if age<18:
        print("Under 18")
        break
    if age>18 and age <60:
        print("Above 18")
        continue
    if age>60:
        pass

while age>18 and age<60:
    print("Eligible to vote")
    break
else:
    print("Not eligible to vote")

if age>18 and age<60:
    for slot in range(6,12,1):
        print("Slots=",slot,"pm -",slot+1,"pm")
    else:
        print("Select Slot")
