class Node:

    def __init__(self,value):
        self.data=value
        self.next=None

new_node1=Node(1)
new_node2=Node(2)

#here we are printing the value of each node
print(new_node1.data)
print(new_node2.data)

#as these nodes are not interconnected therefore the next of both nodes will be none
print(new_node1.next)
print(new_node2.next)

  
