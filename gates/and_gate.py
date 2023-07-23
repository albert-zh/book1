import numpy as np

# this is an and gate
# y = 0 (b + wx <= 0)
# y = 1 (b + wx > =)

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    value = np.sum(w*x) + b
    if value <= 0:
        return 0
    else:
        return 1


    