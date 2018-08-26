def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 24659183668299994531
    q = 28278904334302413829
    e = 11
    ct = 589000442361955862116096782383253550042

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