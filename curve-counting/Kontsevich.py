from scipy import special
c = lambda n,k: special.binom(n,k)
K=[0,1]
def Nd(d):
    sum=0
    for i in range(1,d):
        sum+=K[i]*K[d-i]*(i*i*(d-i)*(d-i)*c(3*d-4,3*i-2)-i*i*i*(d-i)*c(3*d-4,3*i-1))
    return sum

def Kontsevich(n):
    while len(K)<=n:
        K.append(Nd(len(K)))

Kontsevich(15)

for i in K:
    print(i)
