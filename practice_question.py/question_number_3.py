#print prime number from 1 to 500

print("1")
for num in range(1,501):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
         print(num)
         