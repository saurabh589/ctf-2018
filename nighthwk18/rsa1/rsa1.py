def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 31633324922152208667782365945327593684774069143774669661619572762724400715661831 
    q = 36515984267977612350498121647561131263792046107668364547689126140974588406556229 
    e = 65537
    ct = 385039965945614490905402335622210470347499810343020510328873859454424507532623252932642491630030372490846191037269295383730831605896115604912885466639330684242

    # compute n
    n = p * q
    print n

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a
    d = d % phi
    if (d < 0):
        d += phi

    print( "d:  " + str(d) );

    pt = hex(int(pow(ct, d, n)))[2:-1].decode("hex")
  #  pt = pow(ct, d, n)
    print( "flag: " + str(pt) )

if __name__ == "__main__":
     main()