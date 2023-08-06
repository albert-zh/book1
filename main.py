import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image
import gates.gate_test as gate
import activate_function.activate_test as activate
from dataset.mnist import load_mnist
from mnist_predict import mnist_predict as mnist


def showImage():
    img = imread('./dataset/lena.png')
    plt.imshow(img)
    plt.show()


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def mnist_show(x_train, t_train):
    for i in range(10):
        img = x_train[i]
        img = img.reshape(28, 28)
        label = t_train[i]
        print(label)
        img_show(img)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # gate.gate_test()
    # activate.activate_function_test()

    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    network = mnist.init_network("./mnist_predict/sample_weight.pkl")
    accuracy_cnt = 0
    for i in range(len(x_test)):
        y = mnist.predict(network, x_test[i])
        p = np.argmax(y)
        if p == t_test[i]:
            accuracy_cnt += 1
    print("Accuracy:" + str(float(accuracy_cnt) / len(x_test)))
    # mnist_show(x_train, t_train)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
