def main():
    vector_a = [1, 2, 12, 4]
    vector_b = [2, 4, 2, 8]

    scalar_product = 0

    for i in range(0, len(vector_a)):
        scalar_product += vector_a[i] * vector_b[i]

    print(scalar_product)


if __name__ == '__main__':
    main()
