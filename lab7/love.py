import leet as leet


def leet_speak():
    leet = {'o': '0', 'l': '1', 'e': '3', 'a': '4', 't': '7', 's': 'Z'}
    open_file = open("leet.txt", "r")
    my_string = open_file.read()
    new_string = "".join(leet.get(k, k) for k in my_string)
    a = ""
    for line in new_string.split(' \n'):
        for word in line.split(' '):
            a += '(' + word + ') '
        a += "\n"

    print(a)

    outF = open("output_File.txt", "w")
    outF.writelines(a)
    outF.close()


def main():
    leet_speak()


main()
