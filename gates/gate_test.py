import gates.xor_gate as xor

def gate_test():
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = xor.XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))