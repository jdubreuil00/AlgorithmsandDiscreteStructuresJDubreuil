import csv
"""
Module 02 Programming Assignment 02
Jordan Dubreuil
5/22/2023

This program uses a linked list implementation of a stack to read
names from a csv file and add those names to the stack.

Once the names are added to the stack the user is prompted to
enter an integer 1-4. The number indicated how many users are removed
from this last in last out LIFO stack. The remaining user is printed
to the console and the program continues to ask for integers until 
all the names are removed from the stack.
"""
# Imports the csv file
filepath = "A2/People.csv"
# Opens the file
peoplefile = open(filepath,'r')
# Reads the csv file data
readfile = csv.reader(peoplefile)

# Node class for the linked list
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None

#ADT implementation of the Stack  
class Stack:
    def __init__(self):
        self.head = None
        self.current = self.head
    
    def insert(self, item):
        """
        Inserts Nodes into the stack.
        """
        if self.head is None:
            self.head = Node(item)

        else:
            refer = self.head
            while refer is not None:
                if refer.next is not None:
                    refer = refer.next
                else:
                    refer.next = Node(item)
                    break
    
    def printList(self):
        """
        Prints data that is in the stack
        """
        refer = self.head
        while refer is not None:
            print(refer.value)
            refer = refer.next
    
    def insertIndex(self, index, item):
        """
        (Not Used for Assignment)
        Adds an item at a specific index in the stack
        
        Parameters:
            Index: Desired position of the item in the stack
            Item: Data to be inserted in the stack

        Rerurns:
            None
        """
        if self.head is None:
            self.head = Node(item)
        else:
            if index == 0:
                node = Node(item)
                node.next = self.head
                self.head = node
            else:
                refer = self.head
                for i in range(index-1):
                    if refer.next is not None:
                        refer = refer.next
                node = Node(item)
                node.next = refer.next
                refer.next = node

    def removeItem(self):
        """
        Removes the last item from the stack
        """
        if self.head is None:
            print("The list is empty")
            return
        current = self.head
        if current.next is None:
            self.current = self.head
            self.head = None
        
        else:
            while current.next is not None:
                
                nextItem = current.next
                if nextItem.next is None:
                    current.next = None
                    break
                current = current.next
        self.current = current



if __name__=='__main__': 
    # Creates a new instance of the stack   
    stack = Stack()
    # Loops through everyone in the CSV file and adds them to the stack 
    for person in readfile:
        if person[0].startswith("\ufeff"):
            person[0] = person[0][1:]
        stack.insert(person)
    # Prints out the list of people in the stack  
    stack.printList()
    # Asks for a valid integer
    while True:
        try:
            # Asks for a valid integer
            x = int(input("Please enter an integer value between 1 and 4... "))
        except ValueError:
            # Validate input
            print('Sorry please try a valid integer...')
            continue
        if x >=1 and x <= 4:
            # Validates input between 1 and 4
            for item in range(x):
                stack.removeItem() 
            # Checks to see if stack is stack is empty and prints it to the console 
            if stack.head is None:
                print("Stack empty.")
                break 
            # Prints last item in the stack to the console 
            print(stack.current.value)  
            continue
        else:
            # Asks the user for the correct value
            print("Enter an integer between 1 and 4")
            continue