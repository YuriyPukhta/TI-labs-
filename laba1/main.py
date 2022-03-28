import math
from random import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread, imshow
from skimage import data
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage.feature import greycomatrix
import skimage
import skimage.measure
from PIL import Image

def list_made():
    size = randint(10, 20)
    a = [randint(0, 10) for i in range(size)]
    print(a)
    return a


def list_entropy(a, bins_number):
    values, counts = np.unique(a, return_counts=True)
    size = len(a)

    sum = 0
    p_list = []
    for i in counts:
        p = i / size
        # print(p)
        p_list.append( p )
        sum += -1 * p * math.log2(p)
        print(-1 * p * math.log2(p))
    print("my entropy function :",sum)
    return p_list,values, counts

#list_entropy(list_made(), 11)

# C:/Users/Yuriy/Pictures/Screenshots/pac/Pac.png
# C:/Users/Yuriy/Pictures/nyashka.jpg
if __name__ == '__main__':
    img = Image.open('C:/Users/Yuriy/Pictures/nyashka.jpg')

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    greyIm = img.convert('L')
    # plt.figure(num=None, figsize=(8, 6), dpi=80)

    plt.subplot(1, 2, 2)

    plt.imshow(greyIm, cmap=plt.cm.gray)
    plt.show()

    greyIm = np.array(greyIm)
    greyIm_flat = greyIm.flatten()

    print('nyashka.jpg')
    plt.subplot(1, 3, 1)
    p_list,values, counts = list_entropy(greyIm_flat, 256)
    plt.title('nyashka.jpg')
    plt.bar(values, counts)
    entropy = skimage.measure.shannon_entropy(greyIm_flat, base=2)
    print("check entropy =",entropy)


    img = Image.open('C:/Users/Yuriy/Pictures/nyashka.png')
    greyIm = img.convert('L')
    greyIm = np.array(greyIm)
    greyIm_flat = greyIm.flatten()
    print('\nnyashka.png')
    plt.subplot(1, 3, 2)
    plt.title('\nnyashka.png')
    p_list,values, counts = list_entropy(greyIm_flat, 256)
    plt.bar(values, counts)
    entropy = skimage.measure.shannon_entropy(greyIm_flat, base=2)
    print("check entropy =",entropy)


    img = Image.open('C:/Users/Yuriy/Pictures/nyashka.png')
    greyIm = img.convert('L')
    greyIm = np.array(greyIm)
    greyIm_flat = greyIm.flatten()
    print('\nnyashka.bmp')
    plt.subplot(1, 3, 3)
    plt.title('nyashka.bmp')
    p_list,values, counts = list_entropy(greyIm_flat, 256)
    plt.bar(values, counts)


    plt.show()

    entropy = skimage.measure.shannon_entropy(greyIm_flat, base=2)
    print("check entropy =",entropy)





