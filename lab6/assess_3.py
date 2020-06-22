def has_odd(input_set):
    if input_set == {}:
        return False
    else:
        for term in input_set:
            if term % 2 == 1:
                return True
        return False


# empty list
integer_list = []
num_integer = int(input("Enter the number of elements : "))
# scan all items of input values and add into the list
for i in range(0, num_integer):
    ele = int(input())
    integer_list.append(ele)
# convert the list into set
set_of_integers = set(integer_list)
# use the function
result = has_odd(set_of_integers)
print(result)
