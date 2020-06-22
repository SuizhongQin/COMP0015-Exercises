import random


def max_occurrences(input_list):
    if input == list():
        return 0, 0

    else:
        item_set = set(input_list)
        frequency_dict = {}

        for term in item_set:
            frequency_dict[term] = input_list.count(term)

        for key, value in frequency_dict.items():
            if value == max(frequency_dict.values()):
                return key, value


genList = []
for i in range(100):
    num = random.randint(0, 9)
    genList.append(num)

print("The list is: " + str(genList))

mode = max_occurrences(genList)
print("Number " + str(mode[0]) + " appears most frequently - " + str(mode[1]) + " times.")
