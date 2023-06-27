import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

def showImage():
    img = imread('./dataset/lena.png')
    plt.imshow(img)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = np.array([1.0, 2.0, 3.0])
    print(x)

    showImage()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
