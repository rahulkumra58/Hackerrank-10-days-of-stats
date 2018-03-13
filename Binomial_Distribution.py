#Binomial Distribution 1

from math import factorial as fact
p = 0.5216
q = 0.4784

prob= (p/(p+q))

def comb(n,r):
    return fact(n)/(fact(r)* fact(n-r))
n = 6
final_answer = 0
for k in range(3, 7):
    final_answer += prob**k * (1-prob)**(n-k) * comb(n, k) 

print(round(final_answer,3))

#Binomial Distribution 2

def fact(num):
    s=1
    for i in range(1,num+1):
        s *= i
    return s

def binom(n):
    p = 0.12
    q = 0.88
    r = 2

    answer = 0
    for k in range(0, r+1):
        answer += (p**k) * (q**(n-k)) * fact(n)/(fact(k)*fact(n-k))
    print(round(answer,3))
                                         
    answer1 = 0
    for k in range(r, n+1):
        answer1 += (p**k) * (q**(n-k)) * fact(n)/(fact(k)*fact(n-k))
    print(round(answer1,3))

binom(10)