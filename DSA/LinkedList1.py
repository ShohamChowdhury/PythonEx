class node():
    def __init__(self,value=0):
        self.value = value
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = node()
    def append(self,value):
        new_node = node(value)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = new_node
    def length(self):
        curr = self.head
        count = 0
        while curr != None:
            count+=1
            curr = curr.next
        return count
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next!= None:
            cur_node = cur_node.next
            elements.append(cur_node.value)            
        print(elements)
    def get(self,index):
        if index >= self.length():
            print("Error : 'Get' Index out of range!")
            return None
        curr_index = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_index == index : 
                print(curr_node.value)
                return None
            curr_index+=1    
    def erase(self,index):
        if index >= self.length():
            print("Error : 'Get' Index out of range!")
            return None
        curr_index = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_index == index:
                last_node.next = curr_node.next
                return
            curr_index+=1   
        
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.erase(1)
my_list.display()

            