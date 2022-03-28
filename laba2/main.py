from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure

from nearest_neighbor_laba2 import resize_func
from new_2_laba import disc_func
from quantization_laba2 import quantization
from bilinear_laba2 import bl_resize
from new_bicubic import bicubic
from CE import cEntropy

def tesk_3(greyIm):
    _cEntropy = cEntropy(greyIm, greyIm)
    print(_cEntropy)
    disc = 0
    quan_array = [8, 16, 64]
    for i in range(3):
        disc_img = disc_func(greyIm, disc)
        for j in range(3):
            quan = quan_array[j]
            quan_img = quantization(disc_img, quan)
            plt.subplot(1, 3, j + 1)
            plt.title(f'quantization {quan}')
            plt.imshow(quan_img, cmap=plt.cm.gray)
            entropy = skimage.measure.shannon_entropy(quan_img, base=2)
            _cEntropy = cEntropy(disc_img, quan_img)
            print(f"discretization = {disc}\nquantization = {quan}\nentropy = {entropy}\nConditional entropy = {_cEntropy}\n\n")
        plt.show()
        disc += 2
    return 0

def tesk_3_1(greyIm):
    disc = 0
    quan_array = [8, 16, 64]
    for j in range(3):
        quan = quan_array[j]
        quan_img = quantization(greyIm, quan)
        plt.subplot(1, 3, j + 1)
        entropy = skimage.measure.shannon_entropy(quan_img, base=2)
        _cEntropy = cEntropy(disc_img, quan_img)
        print(f"quantization = {quan}\n entropy = {entropy}\n\n")
        print(f"quantization = {quan}\n Centropy = {_cEntropy}\n\n")
        disc += 2
    return 0


def task_6_1(greyIm):
    for i in range(1,3):
        resize = 2**i
        disc_img = disc_func(greyIm, resize)

        plt.subplot(1, 2, 1)
        plt.title(f'discretization : {resize}')
        plt.imshow(disc_img, cmap=plt.cm.gray)


        new_img = resize_func(disc_img, resize)

        plt.subplot(1, 2, 2)
        plt.title(f'bl_resize : {resize}')
        plt.imshow(new_img, cmap=plt.cm.gray)
        plt.show()
    return 0


def task_6_2(greyIm):
    for i in range(1,3):
        resize = 2**i
        disc_img = disc_func(greyIm, resize)

        plt.subplot(1, 2, 1)
        plt.title(f'discretization : {resize}')
        plt.imshow(disc_img, cmap=plt.cm.gray)


        new_img = bl_resize(disc_img, resize)

        plt.subplot(1, 2, 2)
        plt.title(f'bl_resize : {resize}')
        plt.imshow(new_img, cmap=plt.cm.gray)
        plt.show()
    return 0


def task_6_3(greyIm):
    for i in range(1,3):
        resize = 2**i
        disc_img = disc_func(greyIm, resize)

        plt.subplot(1, 2, 1)
        plt.title(f'discretization : {resize}')
        plt.imshow(disc_img, cmap=plt.cm.gray)


        new_img = bicubic(disc_img, resize, a = -1/2)

        plt.subplot(1, 2, 2)
        plt.title(f'bicubic : {resize}')
        plt.imshow(new_img, cmap=plt.cm.gray)
        plt.show()
    return 0





img = Image.open('C:/Users/Yuriy/Pictures/nyashka.png')
greyIm = img.convert('L')
greyIm = np.array(greyIm)
tesk_3(greyIm)