#circular LS with insert at begin
#2.insert at begin
class node:
    def __init__(x,val):
        x.val=val
        x.next=None
head=None
n=int(input("Enter the size of CLL"))
for i in range(n):
    val=int(input("Enter the value"))
    nn=node(val)
    if head is None:
        head=nn
        nn.next=head
    else:
        temp=head
        while temp.next!=head:
            temp=temp.next
        nn.next=head
        temp.next=nn
        head=nn
temp=head
while temp.next!=head:
    print(temp.val,end='->')
    temp=temp.next
print(temp.val,end='->')
print(head.val)

output:-
    Enter the size of CLL5
    Enter the value1
    Enter the value2
    Enter the value3
    Enter the value4
    Enter the value5
    5->4->3->2->1->5
