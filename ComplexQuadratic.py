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
    a = num[0] / den[0] if num[0] % den[0] == 0 else (num[0], den[0])
    b = num[1] / den[0] if num[1] % den[0] == 0 else (num[1], den[0])
    return (a, b)

def add_complex(c1, c2):
    return op_complex(c1, c2, op_add)

def subtr_complex(c1, c2):
    return op_complex(c1, c2, op_subtr)

def mult_complex(c1, c2):
    return op_complex(c1, c2, op_mult)

def div_complex(c1, c2):
    return op_complex(c1, c2, op_div)


# Quadratic formula
# x = - b +/ sqrt(b^2 - 4ac)
#     --------------------
#          2a
def quadratic_form(a,b,c):
    discr = b**2 - 4 * a * c
    print discr
    if discr == 0: return -b / (2 * a)
    
    if not discr < 0:
        root  = m.sqrt(discr)
        return ((-b - root) / (2 * a), (-b + root) / (2 * a))
    
    root = m.sqrt(abs(discr))
    return (div_complex((-b, - root), (2 * a, 0)), div_complex((-b, root), (2 * a, 0)))
loan = -46737
n = 29
p = 464
print 3 % 10