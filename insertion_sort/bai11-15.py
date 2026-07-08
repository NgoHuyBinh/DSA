# BÀI 11
# Sắp xếp theo trị tuyệt đối (ổn định)
def bai_11(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and abs(a[j]) > abs(key):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 11:", bai_11([-3, 1, -2, 2]))

print("-" * 30)

# BÀI 12
# Sắp xếp chuỗi theo độ dài
def bai_12(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and len(a[j]) > len(key):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 12:", bai_12(['abc', 'a', 'ab']))

print("-" * 30)

# BÀI 13
# Tính ổn định
def bai_13(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 13:", bai_13([(2,'a'),(1,'b'),(2,'c')]))

print("-" * 30)

# BÀI 14
# Học sinh theo điểm giảm dần,
# nếu bằng điểm thì tên tăng dần
def bai_14(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and (
            a[j][1] < key[1] or
            (a[j][1] == key[1] and a[j][0] > key[0])
        ):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 14:", bai_14([('An',8),('Ba',9),('Cu',8)]))

print("-" * 30)

# BÀI 15
# Insertion Sort Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_sorted(head, node):
    if head is None or node.data < head.data:
        node.next = head
        return node

    cur = head

    while cur.next and cur.next.data < node.data:
        cur = cur.next

    node.next = cur.next
    cur.next = node

    return head


def insertion_sort_list(head):
    sorted_head = None

    while head:
        nxt = head.next
        head.next = None
        sorted_head = insert_sorted(sorted_head, head)
        head = nxt

    return sorted_head


print("Bài 15: Linked List Insertion Sort")

print("-" * 30)