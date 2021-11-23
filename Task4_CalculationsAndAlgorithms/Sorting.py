import random


def bubble_sort(table):
    n = len(table)
    for i in range(0, n-1):
        for j in range(1, n-i):
            if table[j-1] > table[j]:
                temp = table[j]
                table[j] = table[j-1]
                table[j-1] = temp
    return table


def main():
    random_table = []
    for i in range(0, 50):
        random_table.append(random.randint(0, 100))

    print(random_table)

    bubble_sort_tab = bubble_sort(random_table)
    print(bubble_sort_tab)

    random_table.sort()
    print(random_table)


if __name__ == '__main__':
    main()
