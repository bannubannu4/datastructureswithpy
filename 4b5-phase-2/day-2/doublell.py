class node:
    def __init__(self,data):
        self.data=data
        self.previous=None
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
                print(temp.data,"<==>",end=" ")
                temp=temp.next
obj=SLL()
n1=node(100)
obj.head=n1
n2=node(200)
obj.head.next=n2
n2.prev=n1
n1.next=n2
obj.display()