import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import gates.gate_test as gate
import activate_function.activate_test as activate

def showImage():
    img = imread('./dataset/lena.png')
    plt.imshow(img)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gate.gate_test()
    activate.activate_function_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
