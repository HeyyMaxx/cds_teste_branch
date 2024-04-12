def gather_data():
    n1 = int(input("Primeiro Valor:"))
    n2 = int(input("Segundo Valor:"))

    return n1, n2


def print_message(n1, n2):
    print(f'the values {n1} and {n2} added up result in {n1+n2}')


def main():
    n1, n2 = gather_data()

    print_message(n1, n2)
    return None


if __name__ == "__main__":
    main()
