import math as m

def op_add(a, b):   return a + b
def op_subtr(a, b): return a - b
def op_mult(a, b):  return a * b
def op_div(a, b):   return float(a) / b

def op_complex(c1, c2, o):
    if o == op_add or o == op_subtr:
        return (o(c1[0],c2[0]), o(c1[1],c2[1]))

    if o == op_mult:
        return (o(c1[0], c2[0])-o(c1[1], c2[1]), o(c1[0], c2[1]) + o(c1[1], c2[0]))

    num, den = (op_complex(c1, (c2[0], -c2[1]), op_mult), op_complex(c2, (c2[0], -c2[1]), op_mult))
    return ((num[0], den[0]), (num[1], den[0]))

def add_complex(c1, c2):
    return op_complex(c1, c2, op_add)

def subtr_complex(c1, c2):
    return op_complex(c1, c2, op_subtr)

def mult_complex(c1, c2):
    return op_complex(c1, c2, op_mult)

def div_complex(c1, c2):
    return op_complex(c1, c2, op_div)