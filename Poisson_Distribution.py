#POISSON DISTRIBUTION 1

lamb = float(input())
k = int(input())
e= 2.71828

def fact(c):
    n = 1
    for i in range(1,c+1):
        n*=i
    return n

formula= ((lamb)**k) * (e**-(lamb))/ fact(k)
print(round(formula,3))


#POISSON DISTRIBUTION 2
A= list(map(float, input().split())) 

lamb1 = A[0]
lamb2 = A[1]


CA =160 + 40*(lamb1 + (lamb1)**2) 
CB = 128 + 40*(lamb2 + (lamb2)**2)
print(round(CA,3))
print(round(CB,3))
