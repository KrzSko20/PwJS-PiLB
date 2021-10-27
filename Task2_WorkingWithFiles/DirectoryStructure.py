import os


def directory_tree(path):
    print("\n" + path)
    print(os.listdir(path))
    prev_path = os.path.dirname(path)
    if prev_path != path:
        directory_tree(prev_path)


def main():
    path = r"C:/Program Files/"
    directory_tree(path)


if __name__ == '__main__':
    main()
