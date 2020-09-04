def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)

# "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width) is a string formatter that will convert a number to each of the cases and space each number dynamically according to the "width" value
