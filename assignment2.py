#1)Arithmetic operator______________________________________________________

num1 = int(input("Enter 1st operand="))
num2 = int(input("Enter 2nd operand="))
print("Addition=",num1+num2)
print("Subtraction=",num1-num2)
print("Multiplication=",num1*num2)
print("Division=",num1/num2)
print("Module=",num1%num2)
print("Floor divison=",num1//num2)
print("exponent=",num1**num2)

#2)Assignment operator________________________________________________________
a=10
a += 5
print(a)
a=10
a -= 5
print(a)
a*=1
print(a)
a = 10
a/=1
print(a)
a = 10
a**=1
print(a)
a = 10
a//=1
print(a)
a%=1
print(a)

#3)logical operator_____________________________________________________________

a = False
b = True
print("And=",a and b)
print("OR=",a or b)
print("NOT=",not b)

#4)comparison operator__________________________________________________________

a=int(input("Enter number="))
b=int(input("Enter 2nd number="))
if a>b:
    print(a," is greater")
if a<b:
    print(b," is greater")
if a==b:
    print(a,"Is equal to",b)
if a!=b:
    print(a,"not equal to ",b)
if a>=b:
    print(a,"more than equal to ",b)
if a<=b:
    print(a,"less than equal to ",b)

#5)Bitwise operator
a = 10
b = 5
print("bitwise a & b=",a&b)
print("bitwise a | b=",a|b)
print("bitwise a  b=",a^b)
print("bitwise a >> b=",a>>b)
print("bitwise a << b=",a<<b)

#6)Identity operator______________________________________________________________

a = 10
b = 5
print("is=",a is b)
print("IS NOT=",a is not b)

#7)Membership operator____________________________________________________________

a = "sairaj"
print("IN=","s" in a)
print("NOT IN","s" not in a)


