def min_passes_from_states(initial, current):
    sorted_initial = sorted(initial)
    n = len(initial)
    matched_at_end = 0
    for i in range(n-1, -1, -1):
        if current[i] == sorted_initial[i]:
            matched_at_end += 1
        else:
            break
    return matched_at_end

dau = [4, 3, 2, 1]
sau = [3, 2, 1, 4]
print(min_passes_from_states(dau, sau))