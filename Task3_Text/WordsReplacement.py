def main():
    replacement = {
        "i": "oraz",
        "oraz": "i",
        "nigdy": "prawie nigdy",
        "dlaczego": "czemu"
    }

    file = open('TextFile.txt', 'r')
    text = file.read()
    file.close()

    print(text)

    text = text.replace(".", " .")
    text = text.replace(",", " ,")
    text = text.split()

    for i in range(0, len(text)):
        for x in replacement:
            if text[i] == x:
                text[i] = replacement[x]
                break

    text = " ".join(text)

    print(text)


if __name__ == '__main__':
    main()
