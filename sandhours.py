n=int(input("Enter the number"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print("*",end=" ")
        else:
            if i==j or i+j==n-1 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

* * * * * * * *  
  *           *   
    *       *     
      *   *       
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * *  
