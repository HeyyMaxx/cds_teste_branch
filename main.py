import test

def gather_data_alternate():
    n1 = int(1265)
    n2 = int(300)
    op = '/'

    return n1, n2, op


def gather_data():
    n1 = int(input("First Value:"))
    n2 = int(input("Second Value:"))
    op = input("Operation:")

    return n1, n2, op


def main():
    n1, n2, op = gather_data_alternate()

    print(eval(n1+op+n2))
    return None


if __name__ == "__main__":
    main()
