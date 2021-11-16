def main():
    file = open('TextFile.txt', 'r')
    text = file.read()
    file.close()

    print(text)

    text = text.replace(' sie ', ' ')
    text = text.replace(' i ', ' ')
    text = text.replace(' oraz ', '')
    text = text.replace(' nigdy ', '')
    text = text.replace(' dlaczego ', '')

    print(text)


if __name__ == '__main__':
    main()
