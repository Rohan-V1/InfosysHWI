class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)
    


Head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

Head.next = A

A.next = B

B.next = C

C.next = None

# print(Head)
# print(Head.next)
# print(A.next)
# print(B.next)
# print(C.next)

def display():
    curr = Head
    elements = []

    while curr:
        elements.append(str(curr)) 
        curr = curr.next
    print(' -> '.join(elements))

def search(head,element):
    curr = head

    while curr:
        if element == curr:
            return True
        curr = curr.next
    
    return False





display()

print(search(Head , 2 ))