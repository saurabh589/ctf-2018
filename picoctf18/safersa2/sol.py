def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

 
    p = 128560694465711843998642629641110853033 
    q = 97625680978671329028071161980969374695621

    e = 65537
    ct = 10422324323877703722566707391458023080471412917680448287621011338669272536229518 


   
    n = p * q
    print n

    
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a
    d = d % phi
    if (d < 0):
        d += phi

    print( "d:  " + str(d) )

    pt = hex(int(pow(ct, d, n)))[2:-1].decode("hex")
    # pt = pow(ct, d, n)
    print( "flag: " + pt )

if __name__ == "__main__":
    main()