" Reverse the direction of a linked_list"
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def reverse(linked_list):
    starting_point = linked_list.head
    new_child = None
    new_parent = None
    while starting_point.next is not None:
        new_parent = starting_point.next
        starting_point.next = new_child
        new_child = starting_point
        starting_point = new_parent

    starting_point.next = new_child
    linked_list.head = starting_point
    return linked_list

if __name__ == "__main__":
    list1 = LinkedList()
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")

    node1.next = node2
    node2.next = node3
    list1.head = node1

    first_node = list1.head
    while first_node.next is not None:
        print(first_node.data)
        print("|")
        first_node = first_node.next
    print(first_node.data)

    print("now we reverse:")
    list1 = reverse(list1)
    first_node = list1.head
    while first_node.next is not None:
        print(first_node.data)
        print("|")
        first_node = first_node.next
    print(first_node.data)



     