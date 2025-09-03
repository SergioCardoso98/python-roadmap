#python doesnt have them

#contrary to arrays
    # items can be place anywhere in the memory
    # dinamic size can keep on adding elements to list
    # not need to be the same type

#contrary to lists the linked list "data blocks" in the memory dont need to be together, so when we append we dont move the whole list

#are basicly set of elements/nodes
    #has 2 parts
        #data itself
        #memory address to the next node
    #is a little bigger in terms of space
    #tail has memory adress = NULL

#1st in the list = HEAD
#last = TAIL

#what can we do:
    #insert element everywhere
        #head
            # put address of current head in the new head
        #tail
            #make the node and make tail to the new node and null in the new tail
        #middle
            #make new element refer to the next node and the previous node point to the new
    #delete everuwhere
        #same logic above

#when transversing a element in the middle you cant just acessing it, you have to go from the HEAD untill the node you want

#single linked list
    # node = DATA + NEXT NODE ADDRESS

#Doubly linked list
    # node = PREVIOUS NODE ADDRESS + DATA + NEXT NODE ADDRESS
        #head will have a NULL

#Circular linked list
    # last node links to the beggining

#Doubly Circular linked list
    # same as above but doubled

#very basic logic
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

# Usage example
ll = LinkedList()
ll.insert_head(5)
ll.insert_tail(10)
ll.insert_head(2)
ll.print_list()  # Output: 2 -> 5 -> 10 -> NULL
