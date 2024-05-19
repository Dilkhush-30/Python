#write a program to find factorial of a number given by user
num= int(input("Enter the number :"))
fact=1
for i in range(1,num+1):
    fact = fact*i
print("Factorial number is :",fact)
3