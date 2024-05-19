#write a program to check the given number is palindrome or not

number =input("Enter the number :")
if number == number[::-1]:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome number")
    