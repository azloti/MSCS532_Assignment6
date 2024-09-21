# An Array is a collection of elements where each element is identified by an index
class Array:

    # Create the inner data structure, a dictionary
    def __init__(self): 
        self.length = 0
        self.data = {}

    # Print the dictionary
    def __str__(self):
        return str(self.__dict__)

    # Get the value at a given index
    def get(self, index):
        return self.data[index]

    # Set the value at a given index
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    # Delete the value at a given index
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    # Insert a value at a given index
    def delete(self, index):

        # Store the value to be deleted
        deleted_item = self.data[index]

        # Shift all the values to the left
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        # Delete the last value
        del self.data[self.length - 1]

        # Update the length
        self.length -= 1

        # Return the deleted value
        return deleted_item
    
# Matrix implementation
class Matrix:

    # Create the inner data structure, a dictionary
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.data = {}

    # Print the dictionary
    def __str__(self):
        return str(self.__dict__)

    # Get the value at a given row and column
    def get(self, row, column):
        return self.data[(row, column)]

    # Set the value at a given row and column
    def set(self, row, column, value):
        self.data[(row, column)] = value

    # Delete the value at a given row and column
    def delete(self, row, column):
        # Store the value to be deleted
        deleted_item = self.data[(row, column)]

        # Delete the value
        del self.data[(row, column)]

        # Return the deleted value
        return deleted_item
    
# In a stack, the last element added is the first element to be removed
class Stack:

    # Create the inner data structure, an Array defined above
    def __init__(self):
        self.array = Array()

    # Print the dictionary
    def __str__(self):
        return str(self.__dict__)

    # Add an element to the stack
    def push(self, item):
        self.array.push(item)

    # Remove the last element added to the stack
    def pop(self):
        return self.array.pop()

    # Get the last element added to the stack
    def peek(self):
        return self.array.get(self.array.length - 1)

    # Check if the stack is empty
    def is_empty(self):
        return self.array.length == 0
    
# In a queue, the first element added is the first element to be removed
class Queue:
    def __init__(self):
        self.array = Array()

    def __str__(self):
        return str(self.__dict__)

    # Add an element to the queue
    def enqueue(self, item):
        self.array.push(item)

    # Remove the first element added to the queue
    def dequeue(self):
        return self.array.delete(0)

    # Get the first element added to the queue
    def peek(self):
        return self.array.get(0)

    # Check if the queue is empty
    def is_empty(self):
        return self.array.length == 0

# A linked list is a collection of nodes where each node contains a value and a reference to the next node

# Node class, contains a value and a reference to the next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list class
class LinkedList:

    def __init__(self):
        self.head = None # The first node in the linked list
        self.tail = None # The last node in the linked list
        self.length = 0 # The number of nodes in the linked list

    def __str__(self):
        return str(self.__dict__)

    # Add a node to the end of the linked list
    def append(self, value):
        # Create a new node
        new_node = self.Node(value)

        # If the linked list is empty, set the new node as the head and the tail
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else: # Otherwise, set the new node as the next node of the tail and update the tail
            self.tail.next = new_node
            self.tail = new_node

        # Update the length
        self.length += 1

    # Add a node to the beginning of the linked list
    def prepend(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # Insert a node at a given index
    def insert(self, index, value):
        if index == 0: # If the index is 0, prepend the value
            self.prepend(value)
            return
        if index >= self.length: # If the index is greater than or equal to the length, append the value
            self.append(value)
            return
        new_node = self.Node(value) # Create a new node
        leader = self.traverse_to_index(index - 1) # Traverse to the node before the index
        new_node.next = leader.next # Set the next node of the new node to the next node of the leader
        leader.next = new_node # Set the next node of the leader to the new node
        self.length += 1 # Update the length

    # Delete a node at a given index
    def delete(self, index):
        leader = self.traverse_to_index(index - 1) # Traverse to the node before the index
        deleted_node = leader.next # Store the node to be deleted
        leader.next = deleted_node.next # Set the next node of the leader to the next node of the deleted node
        self.length -= 1 # Update the length
        return deleted_node # Return the deleted node

    # Traverse to a given index
    def traverse_to_index(self, index):
        # If the index is out of bounds, return the last node
        current_node = self.head

        # Traverse to the node at the given index
        for i in range(index):
            current_node = current_node.next

        # Return the node at the given index
        return current_node

