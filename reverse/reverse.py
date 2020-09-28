class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #Assign a variable to the starting point for a while loop
        current = self.head
        #Assign a variable to be a type of 'previous' attribute.  First node in array must be None since it will be the last node in array when finished while loop
        prev = None
        #Check for a head
        next = None
        if not self.head:
            #return if head not found
            return 
        #WHile loop based on a current position
        while current:
            #store the value of the next_node attribut for later use when assigning the next node in while loop
            next = current.next_node
            #Assign the current next_node attribute to the previous node via the "prev" variable.  
            current.next_node = prev
            #Change the prev variable to the current node for the next itereation
            prev = current
            #Change the current variable so the while loop will move to the next node
            current = next 
        #Assign the head to the last prev variable in the loop. This affectively finishes the code block by assigning the head to the former tail.
        self.head = prev
