# coding: utf-8
from gates.and_gate import AND
from gates.nand_gate import NAND
from gates.or_gate import OR

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
