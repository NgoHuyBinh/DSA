def bai_11():
    a = [(2, 'a'), (2, 'b'), (1, 'c')]
    a[0], a[2] = a[2], a[0] 
    print("Bài 11:", a) 

print("-"*30)

def bai_12(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]: min_idx = j
        min_val = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = min_val
    return a
print(bai_12([(2, 'a'), (2, 'b'), (1, 'c')]))

print("-"*30)

def bai_13(students):
    n = len(students)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][1] < students[min_idx][1]: min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]
    return students
print(bai_13([('Toán', 8), ('Văn', 5)]))

print("-"*30)

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def bai_14():
    print("Bài 14: 1 -> 2 -> 3 -> null")
bai_14()

print("-"*30)

def bai_15(a, k):
    n = len(a)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
print(bai_15([5, 3, 1, 4, 2], 2))