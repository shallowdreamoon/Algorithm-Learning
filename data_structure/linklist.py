
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

#创建链表

#头插法
def print_linklist(lk): #lk指的是头指针
    while lk:
        print(lk.item,end=',')
        lk=lk.next

def create_linklist_head(li):
    head=Node(li[0])
    for element in li[1:]:
        node=Node(element)
        node.next=head
        head=node
    return head

lk=create_linklist_head([1,2,3,4,5,6])
print_linklist(lk)


#尾插法
def create_linklist_tail(li):
    head=Node(li[0])
    tail=head
    for element in li[1:]:
        node=Node(element)
        tail.next=node
        tail=node
    return head
lk=create_linklist_tail([1,2,3,4,5,6])
print('\n')
print_linklist(lk)
