import ComplexNumbers as cN


def main():
    print("Write equation using the following format: 5 4 * 1 -7")
    input_str = input("The result will be: 5+4j * 1-7j").split(' ')
    num1 = cN.ComplexNumbers(int(input_str[0]), int(input_str[1]))
    num2 = cN.ComplexNumbers(int(input_str[3]), int(input_str[4]))
    res = cN.ComplexNumbers(0, 0)
    operation = input_str[2]

    if operation == '+':
        res = num1 + num2
    elif operation == '-':
        res = num1 - num2
    elif operation == '*':
        res = num1 * num2
    else:
        print("Wrong operation.")

    print(res.print())


if __name__ == '__main__':
    main()
