# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:03:08 2023

@author: Aryaman Kumar
"""
p=257537580059538749076827040674299114427
q=260394370037353415715240670779029180333
lambda1=(p-1)* (q-1)



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
e=65537
d = modinv(e,lambda1)
dp = modinv(e,(p-1))
dq = modinv(e,(q-1))
qi=modinv(q,p)
print(p*q)
print(d)
print(dp)
print(dq)
print(qi)
