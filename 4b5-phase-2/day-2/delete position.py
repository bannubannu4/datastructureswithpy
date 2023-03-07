class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("LL is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"===>",end=" ")
                temp=temp.next
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
            
obj=SLL()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
obj.display()
print()
obj.delete()
obj.display()