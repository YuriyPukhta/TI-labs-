from PIL import Image
import matplotlib.pyplot as plt

import numpy as np





def disc_func(greyIm , disc = 8):

    if disc == 0:
        plt.subplot(1, 2, 1)
        plt.title('original')
        plt.imshow(greyIm, cmap=plt.cm.gray)

        plt.subplot(1, 2, 2)
        plt.title(f'discretization: {disc}')
        plt.imshow(greyIm, cmap=plt.cm.gray)

        plt.show()
        return greyIm

    height = greyIm.shape[0]
    width = greyIm.shape[1]
    disc_h = int(height/disc)
    disc_w = int(width/disc)
    numHeight = int(height/disc_h)
    numwidth = int(width/disc_w)
    new_img = np.zeros((disc_h, disc_w), np.uint8)
    #new_img = np.zeros((height, width, 1), np.uint8)
    # Image cyclic sampling 8*8 Area
    for i in range(disc_h):
        y = i*numHeight
        for j in range(disc_w):
            x = j*numwidth

            im = greyIm[y, x]
            new_img[i, j] = np.uint8(im)



    return new_img


def show_dics_plot(greyIm,disc ):
    plt.subplot(1, 2, 1)
    plt.title('original')
    plt.imshow(greyIm, cmap=plt.cm.gray)

    plt.subplot(1, 2, 2)
    plt.title(f'дискретизаці: {disc}')
    plt.imshow(new_img, cmap=plt.cm.gray)
    plt.show()
'''
        for n in range(numHeight):
            for m in range(numwidth):
                new_img[y + n, x + m] = np.uint8(i)'''

if __name__ == '__main__':
    img = Image.open('C:/Users/Yuriy/Pictures/nyashka.png')
    greyIm = img.convert('L')
    greyIm = np.array(greyIm)

    new_img = disc_func(greyIm, 0)
# Display images

