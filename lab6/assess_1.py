# a function called print_palindrome that prompts the user to enter one or
# more words and prints whether the entered string is a palindrome


def print_palindrome(string):
    str_1 = string.lower()
    str_2 = str_1[::-1]
    return str_1 == str_2


print(print_palindrome("1991"))
