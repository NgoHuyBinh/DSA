def last_element_after_1_pass(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a[-1]

a = [4, 2, 7, 1, 3]
print(last_element_after_1_pass(a))