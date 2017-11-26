

class node:
    """ Passing the data pointer and setting the default to none"""
    def __init__(self,data=None):
        self.data=data
        self.next=None
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

