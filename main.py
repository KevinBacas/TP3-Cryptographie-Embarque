from utils import verifie_point, addition_points, double_and_add, groupe_des_points

if __name__ == "__main__":
    print "Hello world!"

    print "verifie_point(3, 2, 5, (0, 0))", verifie_point(3, 2, 5, (0, 0))
    print "verifie_point(3, 2, 5, (2, 1))", verifie_point(3, 2, 5, (2, 1))
    print "verifie_point(3, 2, 5, (2, 2))", verifie_point(3, 2, 5, (2, 2))

    print "(2,1) + (2,4) =", addition_points(3, 2, 5, (2,1), (2,4))
    print "(2,1) + (2,1) =", addition_points(3, 2, 5, (2,1), (2,1))
    print "(2,1) + (0,0) =", addition_points(3, 2, 5, (2,1), (0,0))
    print "(2,1) + (1,1) =", addition_points(3, 2, 5, (2,1), (1,1))
    print "(2,1) + (1,4) =", addition_points(3, 2, 5, (2,1), (1,4))
    print "(1,4) + (1,4) =", addition_points(3, 2, 5, (1,4), (1,4))

    P = (2,4)
    for i in xrange(6):
        print i, "*", P, "=", double_and_add(3, 2, 5, P, i)

    print "F5 :", len(groupe_des_points(3, 2, 5))
    print "F11 :", len(groupe_des_points(1, 2, 11))
