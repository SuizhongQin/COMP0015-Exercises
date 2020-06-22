def flip_lines(file):
    open_file = open("file.txt", "r")
    new_string = open_file.read()
    lines = new_string.split('\n')
    length = len(lines)

    output = ""
    pair = length // 2
    last_line = length % 2

    for i in range(pair):
        output += lines[2 * i + 1] + '\n' + lines[2 * i] + '\n'

    if last_line == 1:
        output += lines[length - 1]

    return output


def main():
    print(flip_lines("file.txt"))


main()