def disjoint(m1, m2):
    # either of two dictionaries is empty will return true
    if m1 == {} or m2 == {}:
        return True
    else:
        # extracts all items from two dictionaries
        items_m1 = m1.items()
        items_m2 = m2.items()
        # compares them and find items in common
        # if there is no common items, return true
        if len(items_m1 & items_m2) == 0:
            return True
        else:
            return False


# test part
s1 = {7: 1, 18: 5, 42: 3, 76: 10, 98: 2, 234: 50}
s2 = {7: 1, 11: 9, 42: -12, 98: 4, 234: 0, 9999: 3}
s3 = {7: 2, 11: 9, 42: -12, 98: 4, 234: 0, 9999: 3}
s4 = {}
print(disjoint(s1, s2))
print(disjoint(s1, s3))
print(disjoint(s1, s4))
