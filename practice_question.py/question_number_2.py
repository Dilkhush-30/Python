"""    *
     * * *
   * * * * *
 * * * * * * * 
"""

for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(1,(2*i-1)+1):
        print("*",end=" ")
    print("\n")