#decimal equivalance of 1+1/2+1/3+...1/n
print("EnterITERATIVE VALUE")
n=int(input())
sum=0
for d in range(1,n+1):
    sum=sum+(1/d)
    print("The sum is",sum)