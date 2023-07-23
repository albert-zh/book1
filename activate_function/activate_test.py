import activate_function.relu as relu
import activate_function.sigmoid as sigmoid
import activate_function.step_function as step
import numpy as np
import matplotlib.pylab as plt
def activate_function_test():
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = relu.relu(x)
    y2 = sigmoid.sigmoid(x)
    y3 = step.step_function(x)

    plt.ylim(-1.0, 1.5)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)

    plt.show()



