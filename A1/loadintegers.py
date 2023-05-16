import os
from linkedlist import *

file = open("A1/numbers.txt","r")

content = file.read()
a = []

linestripped = content.split("\n")
# List comprehension
a = [int(line.strip()) for line in linestripped if line.strip()]

a.sort()


L = LinkedList()

for i in range(len(a)):
    L.insertCurrentNext(a[i])
    L.nextCurrent()
    
L.resetCurrent()
L.printList()

while True:
    try:
        # Asks the Canadian for the temperature i  Celsius
        x = int(input("Please enter an integer value..."))
    except ValueError:
        #Validate input
        print('Sorry please try a valid integer...')
        continue
    else:
        # Exits the while loop because input is valid.
        break

current = L.Header
prev = None

while current:
    print(current.Data)
    if current.Data == x:
        if prev is None:
            # If the node to remove is the header node, update the header
            L.Header = current.Next
        else:
            # If the node to remove is not the header node, update the previous node's next pointer
            prev.Next = current.Next
        break
    elif current.Data < x and current.Next and current.Next.Data > x:
        newNode = Node(x)
        newNode.Next = current.Next
        current.Next = newNode
        break

    prev = current
    current = current.Next

L.printList("Press enter to see sorted link list")

