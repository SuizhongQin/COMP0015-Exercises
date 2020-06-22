def find_matches(name, keywords):
    line_cnt = 0
    # creat an empty list
    res = []
    # extract every line
    for line in open(name).readlines():
        line_cnt += 1
        # split them
        sp = line.split()
        found = False
        for word in sp:
            if word in keywords:
                found = True
        if found:
            res.append(line_cnt)
    # return -1 when the list is empty
    if len(res) == 0:
        return [-1]
    return res


# test part
a = ['bird', 'sings']
print(find_matches('angelou.txt', a))
b = ['dinosaur', 'PITS', 'pots']
print(find_matches('angelou.txt', b))
c = ['things', 'caged']
print(find_matches('angelou.txt', c))
