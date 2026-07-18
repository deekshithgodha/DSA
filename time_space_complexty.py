'''print("Hi Student........") # O(1)

a=10
b=20
print(a+b) #TC,SC '''


#Time Complexity: O(n),  space Complexity: O(2) #here we used only 1 loop so its O(n)
'''n=int(input("Enter the number"))
for i in range(n):
    print(i,i+100)'''

#2loops parallelly

#Time complexity N+N=2N, Space Complexity O(1) #here we used 2 loops with same indendation so O(2n)

'''n=int(input("Enter number"))
for i in range(n):
    print("#")
for j in range(n):
    print("$")'''

#Time complexity O(n^3) , Space Complexity O(1) 

'''n=int(input("Enter number"))
for i in range(n):
    for j in range(n):
        for k in range(n):
            print("*",end=' ') #When we keep the another symbol beside * using tuple(), then that type is called the space complexity O(2)
        print()
    print()'''


#Time complexity O(log(N))  , Space Complexity O(1) 
'''n=int(input())
while n>1:
    print(n)
    n//=2
print(n)'''

#time complexity O(log(log(N))), Space Complexity O(1)
n=int(input("Enter the value"))
while n>2:
    print(n)
    n=int(n**0.5)
print(n)



