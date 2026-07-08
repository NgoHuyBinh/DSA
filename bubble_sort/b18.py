class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bubble_sort_linked_list(head):
    if not head:
        return None

    swapped = True
    while swapped:
        swapped = False
        curr = head

        while curr.next:
            if curr.val > curr.next.val:
                curr.val, curr.next.val = curr.next.val, curr.val
                swapped = True
            curr = curr.next

    return head

head = Node(1, Node(3, Node(2)))
head = bubble_sort_linked_list(head)

result = []
while head:
    result.append(str(head.val))
    head = head.next

print("->".join(result) + "->null")