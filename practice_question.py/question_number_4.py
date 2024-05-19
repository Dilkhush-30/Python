#write a program to find factor of a number given by user

number = int(input("Enter number to find factor :"))
for i in range( 1,number+1):
    if(number % i==0):
        print(i)
               