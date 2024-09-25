class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            return

        previous.next = current.next
        current = None

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def roll(self, k):
        if self.head is None or k == 0:
            return

        length = self.count()
        k = k % length
        if k == 0:
            return

        slow = self.head
        fast = self.head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return

        self.head = self._merge_sort_rec(self.head)

    def _merge_sort_rec(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self._merge_sort_rec(head)
        right = self._merge_sort_rec(next_to_middle)

        sorted_list = self._sorted_merge(left, right)

        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head.next

        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next

        return slow

    def _sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)

        return result

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def get(self, i):
        current = self.head
        count = 0
        while current:
            if count == i:
                return current
            count += 1
            current = current.next
        return None

    def insert(self, index, data):
        """Insert a new node with the given data at the specified index."""
        new_node = Node(data)

        if index == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError("Index out of bounds")

        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        """Remove the first node containing the specified data."""
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous is None:
                    # Node to remove is the head
                    self.head = current.next
                else:
                    # Node to remove is in the middle or end
                    previous.next = current.next

                # Special case: if the node to remove is the last node (no next node)
                if current.next is None and previous is not None:
                    previous.next = None

                current = None
                return

            previous = current
            current = current.next

    def __len__(self):
        return self.count()

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return str(elements)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.append(30)
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(40)

    print("Original linked list:")
    linked_list.display()

    print("\nCount of nodes:", len(linked_list))

    # Find a node containing a specific data
    data_to_find = 20
    found_node = linked_list.find(data_to_find)
    print(f"\nFinding data {data_to_find}:")
    if found_node:
        print(f"Node with data {data_to_find} found: {found_node.data}")
    else:
        print(f"Node with data {data_to_find} not found")

    # Get the i-th node
    index_to_get = 2
    node_at_index = linked_list.get(index_to_get)
    print(f"\nGetting the node at index {index_to_get}:")
    if node_at_index:
        print(f"Node at index {index_to_get} has data: {node_at_index.data}")
    else:
        print(f"No node at index {index_to_get}")

    linked_list.reverse()
    print("\nLinked list after reversing:")
    linked_list.display()

    linked_list.roll(2)
    print("\nLinked list after rolling by 2 positions:")
    linked_list.display()

    linked_list.merge_sort()
    print("\nLinked list after sorting using Merge Sort:")
    linked_list.display()

    # Print the linked list using __str__ method
    print(f"\nLinkedList as Python list: {linked_list}")

    linked_list.insert(2, 25)
    print("\nLinked list after inserting 25 at index 2:")
    linked_list.display()

    linked_list.insert(0, 5)
    print("\nLinked list after inserting 5 at the beginning:")
    linked_list.display()

    linked_list.insert(len(linked_list), 50)
    print("\nLinked list after inserting 50 at the end:")
    linked_list.display()

    print("Original linked list:")
    linked_list.display()

    linked_list.remove(10)
    print("\nLinked list after removing 10:")
    linked_list.display()

    linked_list.remove(30)
    print("\nLinked list after removing 30 (head):")
    linked_list.display()

    linked_list.remove(40)
    print("\nLinked list after removing 40 (tail):")
    linked_list.display()

    linked_list.remove(20)
    print("\nLinked list after removing 20 (only node left):")
    linked_list.display()