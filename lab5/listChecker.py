def contains(a1, a2):
    i = 0
    j = 0
    while i < len(a1):
        if a1[i] == a2[j]:
            j += 1
            if j > len(a2) - 1:
                return True
        else:
            j = 0
        i += 1
    return False


print(contains([1, 6, 2, 1, 4, 1, 2, 1, 8], [6, 2, 3]))
