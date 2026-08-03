#Circular Linked list operations insert at end
#ending
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("Enter the size of circular linked list"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:        
        head=newnode        #head=newnode
        tail=newnode          #newnode.next=head
        tail.next=head
    else:
        tail.next=newnode   #temp=head
        tail=newnode           #while temp.next!=head:
        tail.next=head          #temp=temp.next
print("Circular LL")        #newnode.next=head
temp=head                       #temp.next=newnode
while temp.next!=head:      #head=newnode
    print(temp.data,end="-->")
    temp=temp.next
print(temp.data,end="-->")
print(head.data)

    Enter the size of circular linked list5
    Enter the value:1
    Enter the value:2
    Enter the value:3
    Enter the value:4
    Enter the value:5
    Circular LL
    1-->2-->3-->4-->5-->1



