def c ():
    print('C')
    a()


def b():
    print('B')
    c()


def a():
    print('A')
    b()

def main():
    a()


if __name__ == '__main__':
    main()