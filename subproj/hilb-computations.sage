import random
from itertools import izip

class Partition3d(list):
    # A 3d partition, stored as list of row lengths per layer
    def __init__(self, lst, vol=0):
        super(Partition3d, self).__init__(lst)
        self.__vol = vol if vol else sum([n for r in lst for n in r])

    def volume(self):
        return self.__vol

    def cells(self):
        return [(i,j,k) for k, l in enumerate(self) \
                for j, r in enumerate(l) \
                for i in range(r)]

class Partitions3d(list):
    # Enumerates 3d partitions of given volume
    def __init__(self, vol):
        super(Partitions3d, self).__init__(
            [p for constr in Partitions(vol) \
             for base in Partitions(constr[0]) \
             for p in self.__Partitions3dOverBase([base], 1, constr)])
        self.__vol = vol

    def __repr__(self):
        return "3D partitions with volume " + str(self.__vol)

    def __Partitions3dOverBase(self, base, i, constr):
        # Enumerate, with prescribed number of blocks per layer,
        # fitting on top of base which already has i+1 layers
        return ([Partition3d(base)] if i == len(constr) else \
                [p for l in Partitions(constr[i], outer=base[-1]) \
                 for p in self.__Partitions3dOverBase(base+[l], i+1, constr)])

    def list(self):
        return list(self)

    def random_element(self):
        return random.choice(self)

def P3_4_22():
    # Verifying problem 3.4.22 in Andrei's K-theory notes
    R.<t1, t2> = LaurentPolynomialRing(QQ, 't1,t2') # underlying rep'n ring
    l = Partitions(20).random_element()
    V = sum([t1^(-i) * t2^(-j) for (i,j) in l.cells()])
    Vinv = V(t1^(-1), t2^(-1))
    P1 = (V + Vinv*t1*t2 - V*Vinv*(1-t1)*(1-t2))
    P2 = sum([(t1^(-l.leg_length(i,j))*t2^(l.arm_length(i,j)+1) + \
              t1^(l.leg_length(i,j)+1)*t2^(-l.arm_length(i,j))) \
              for (i,j) in l.cells()])
    if P1 == P2:
        print "Checked", l
    return P1

# Exercise 3.4.44 in Andrei's K-theory notes, for given z^n

R.<t1,t2,t3> = LaurentPolynomialRing(QQ, 't1,t2,t3')
var('z1,z2,z3') # Easier to work in SymbolicRing for canceling

Ovir = 0
for p in Partitions3d(2):
    V = sum([t1^-i * t2^-j * t3^-k for (i,j,k) in p.cells()])
    TtM = (t1 + t2 + t3 - 1) * V * V(t1^-1, t2^-1, t3^-1) + V
    TtMwts = [TtM.monomial_coefficient(m) * m(z1,z2,z3) for m in TtM.monomials()]
    Ovir += V(z1,z2,z3) * prod([(1 - w/(z1*z2*z3))/(1 - w^-1) for w in TtMwts])

# P3_4_22()
plot(x^2,(x,0,5)).show()