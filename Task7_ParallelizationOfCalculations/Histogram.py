import matplotlib.pyplot as plt
import threading
import cv2 as cv
import time

start_time = time.time()


def histogram(img, i, histogram_rgb):
    histogram_rgb[i] = (cv.calcHist([img], [i], None, [256], [0, 256]))


def main():
    path = r'Hamburg.jpg'
    img = cv.imread(path)
    col = ('b', 'g', 'r')
    histogram_rgb = [0, 0, 0]

    threads = list()
    for i in range(3):
        t = threading.Thread(target=histogram, args=(img, i, histogram_rgb,))
        threads.append(t)
        t.start()

    for i, thread in enumerate(threads):
        thread.join()
        plt.plot(histogram_rgb[i], color=col[i])

    plt.title("Histogram")
    plt.grid(True)
    plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
