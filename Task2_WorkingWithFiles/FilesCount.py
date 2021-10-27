import os


def main():
    path = "/dev"   # path working on Linux, but not on Windows
    print(len(os.listdir(path)))


if __name__ == '__main__':
    main()
