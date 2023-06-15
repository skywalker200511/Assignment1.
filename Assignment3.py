num1 = int(input("Enter 1st operand="))
num2 = int(input("Enter 2nd operand="))
op = int(input("Choose operator=\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Module\n\n6)exponential\n7)Floor\n"))
if op==1:
    print("Addition=",num1+num2)
elif op==2:
    print("Subtraction=",num1-num2)
elif op==3:
    print("Multiplication=",num1*num2)
elif op==4:
    print("Division=",num1/num2)
elif op==5:
    print("Module=",num1%num2)
elif op==6:
    print("Exponential=",num1**num2)
elif op==7:
    print("Floor=",num1//num2)