

class node:
    """ Passing the data pointer and setting the default to none"""
    def __init__(self,data=None):
        self.data = data
        self.next = None
    """ Wrapper that wraps up the nodes, the user will not interface with the node class """
class linked_list:
    def __init__(self):
        self.head = node()
    """ function that will append the data to the linked list"""
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    """ function that will determined what is the len of the linked list """
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    ''' function to display the current contents of the list '''
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

# my_list = linked_list()
#
# my_list.display()
#
# my_list.append(1)
# my_list.append(2)
#
# my_list.display()

    """ function that will extract a pointer """
    def get(self,index):
        if index>=self.length():
            print("ERROR: 'GET' Index out of range!")
            return None
        cur_indx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_indx==index: return cur_node.data
            cur_indx+=1

# my_list = linked_list()
#
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
#
# my_list.display()
#
# print("element at 2nd index: %d" % my_list.get(2))
#
    ''' erase function that will erase any given node '''
    def erase(self,index):
      if index>=self.length():
          print("ERROR: 'Erase' Index out of range!")
          return
      cur_indx=0
      cur_node=self.head
      while True:
          last_node = cur_node
          cur_node = cur_node.next
          if cur_indx==index:
              last_node.next = cur_node.next
              return
          cur_indx+=1
my_list = linked_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.display()

my_list.erase(3)

my_list.display()
