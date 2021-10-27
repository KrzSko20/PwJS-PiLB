from PIL import Image
import os


def jpg_to_png_conversion(path):
    images = os.listdir(path)

    for a in images:
        a_path = os.path.join(path, a)
        if os.path.isfile(a_path):
            image = Image.open(a_path)
            a_path = a_path.replace('.jpg', '_PNG.png')
            image.save(a_path)


def main():
    path = "D:\Zdjęcia"
    jpg_to_png_conversion(path)


if __name__ == '__main__':
    main()
