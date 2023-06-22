ls = []

for i in range(0,5,1):
    n = int(input("Enter number = "))
    ls.append(n)

print("List: \n",ls)
#1
print("Sum of all elements = ",sum(ls))
#2
print("Smallest number = ",min(ls))
#3
print("Biggest number = ",max(ls))
#4
ls.sort()
print("Ascending = ",ls)
#5
ls.reverse()
print("Descending = ",ls)
#6
ls.sort()
print(tuple(ls))
#7
del ls
