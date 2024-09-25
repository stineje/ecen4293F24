class Node:
    """ A basic node class for storing data """
    def __init__(self, data):
        """ constructor """
        self.value = data


item = Node(3.141592653589793)
print(item.value)
item2 = Node("Hi")
print(item2.value)