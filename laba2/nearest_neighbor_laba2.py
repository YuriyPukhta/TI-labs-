from PIL import Image
import matplotlib.pyplot as plt
from new_2_laba import disc_func
import numpy as np

def resize_func(greyIm ,resize = 8):

    height = greyIm.shape[0]
    width = greyIm.shape[1]
    rHeight =  (resize)
    rWidth =  (resize)
    numHeight = (height*resize)
    numWidth = (width*resize)
    new_img = np.zeros((numHeight, numWidth), np.uint8)
    #new_img = np.zeros((height, width, 1), np.uint8)
    # Image cyclic sampling 8*8 Area
    for i in range(height):
        y = i*rHeight
        for j in range(width):
            x = j*rWidth

            pix = greyIm[i,j]
            for n in range(rHeight):
                for m in range(rWidth):
                    new_img[y + n, x + m] = np.uint8(pix)

    return new_img


if __name__ == '__main__':
    img = Image.open('C:/Users/Yuriy/Pictures/nyashka.png')
    greyIm = img.convert('L')
    greyIm = np.array(greyIm)

    plt.subplot(1, 3, 1)
    plt.title('original')
    plt.imshow(greyIm, cmap=plt.cm.gray)


    greyIm = disc_func(greyIm, 8)

    plt.subplot(1, 3, 2)
    plt.title('original1')
    plt.imshow(greyIm, cmap=plt.cm.gray)

    resize = 8

    new_img = resize_func(greyIm, resize)

    plt.subplot(1, 3, 3)
    plt.title(f'resize by nearest_neighbor : {resize}')
    plt.imshow(new_img, cmap=plt.cm.gray)
    plt.show()
