import math

# IMPORT TP2
def pgcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def bezout(a, b):
    (u0, u1) = (1, 0)
    (v0, v1) = (0, 1)
    while b != 0:
        r = a % b
        q = (a - r) / b
        (a, b) = (b, r)
        (u0, u1) = (u1, u0 - q*u1)
        (v0, v1) = (v1, v0 - q*v1)
    return (a, u0, v0) if a > 0 else (-a, -u0, -v0)

def inverse(a, n):
	res = 0
	if n > 1 and pgcd(a, n) == 1:
		(a, u0, v0) = bezout(a, n)
		res = u0 % n
	# TODO: Afficher un message d'erreur si res == 0
	return res

def verifie_point(A, B, p, P):
    res = False
    if P != (0, 0):
        x, y = P
        # Calcul y^2
        left_op = math.pow(y, 2) % p
        # Calcul X^3 + AX + B
        right_op = (math.pow(x, 3) + A*x + B) % p
        res = left_op == right_op
    else:
        res = True
    return res

def addition_points(A, B, p, P, Q):
    Px, Py = P
    Qx, Qy = Q
    res = (0,0)
    if P == (0,0):
        res = Q
    elif Q == (0,0):
        res = P
    elif Px != Qx:
        lamb = ((Qy-Py)*inverse((Qx-Px), p)) % p
        resx = (math.pow(lamb, 2)-Px-Qx) % p
        resy = (lamb*(Px-resx)-Py) % p
        res = (resx,resy)
    elif Py == Qy:
        if Py != 0:
            lamb = ((3*math.pow(Px, 2)+A)*inverse(2*Py, p)) % p
            resx = (math.pow(lamb, 2)-Px-Px) % p
            resy = (lamb*(Px-resx)-Py) % p
            res = (resx,resy)
    return res

def double_and_add(A, B, p, P, k):
    res = (0,0)
    b = bin(k)[2:]
    for di in b:
        res = addition_points(A, B, p, res, res)
        if (di) == "1":
            res = addition_points(A, B, p, P, res)
    return res

def groupe_des_points(A, B, p):
    res = []
    for x in xrange(p):
        for y in xrange(p):
            point = (x,y)
            if verifie_point(A, B, p, point):
                res.append(point)
    return res
