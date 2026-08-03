'''conversion of SLL from insert insert at begin to insert at end reserve a SLL'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("enter the number of nodes"))
for i in range(n):
    value=int(input("enter the value"))
    new_node=node(value)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        tail=new_node
print("The Original SLL is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")

# Reversing the SLL
prev=None
current=head
while current:
    next=current.next
    current.next=prev
    prev=current
    current=next
head=prev
print("The Reversed SLL is:")
temp=head
while temp.next:
    print(temp.data,end="->")
    temp=temp.next
    
print(temp.data,end="->")
