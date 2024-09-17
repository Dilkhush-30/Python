#INPUT FROM USER TH CHECK IT IS A PALINDROME OR NOT
a=str(input("enter a string to check a palindrome :"))
b=a[::-1]
if a==b:
    print("The letter is a palindrome")
else:
   
   print("The letter is not a palindrome")