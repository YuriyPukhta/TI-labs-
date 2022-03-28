from PIL import Image
import matplotlib.pyplot as plt

import numpy as np




def quantization (greyIm, q):
    height = greyIm.shape[0]
    width = greyIm.shape[1]
    '''
    plt.subplot(1, 2, 1)
    plt.title('original')
    plt.imshow(greyIm, cmap=plt.cm.gray)
    '''
    new_img = np.zeros((height, width), np.uint8)
    min = 0#np.amin(greyIm())
    max = 255#np.amax(greyIm())
    correction = int((max - min)/q)
    step = q
    for y in range(height):
        for x in range(width):
            z = round(greyIm[y,x]/q)
            i = z*step
            new_img[y, x] = np.uint8(i)
    '''
    plt.subplot(1, 2, 2)
    plt.title(f'quantization {q}')
    plt.imshow(new_img, cmap=plt.cm.gray)
    plt.show()
    '''
    return new_img

if __name__ == '__main__':
    img = Image.open('C:/Users/Yuriy/Pictures/nyashka.png')
    greyIm = img.convert('L')
    greyIm = np.array(greyIm)
    for i in range(7):
        quantization(greyIm, 2**i)
    
