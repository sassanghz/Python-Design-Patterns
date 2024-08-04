# an iterator defines the values in an object that can be iterated through
myList = [1,2,3]
for n in myList:
    print(n)

# we can do a different method
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None     

    #Define Iterator
    def __iter__(self):
        self.cur = self.head
        return self   
    
    #Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration
        
#Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
myList = LinkedList(head)

for n in myList:
    print(n)