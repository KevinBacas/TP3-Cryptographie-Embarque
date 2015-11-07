import math

def verifie_point(A, B, p, P):
    res = False
    x = P[0]
    y = P[1]
    z = P[2]
    if z != 0:
        # Calcul y^2
        left_op = math.pow(y, 2) % p
        # Calcul X^3 + AX + B
        right_op = (math.pow(x, 3) + A*x + B) % p
        res = left_op == right_op
    else:
        res = True
    return res

def addition_points(A, B, p, P, Q):
    pass
