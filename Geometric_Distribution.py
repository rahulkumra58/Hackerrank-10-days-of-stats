
#Geometric Distribution Part 1
num_denom = list(map(int, input().split()))
n=int(input())
p= num_denom[0]/num_denom[1]    
def g(n,p):
    ans= (p) * (1-p)**(n-1)
    final_ans = round(ans,3)
    return final_ans

print(g(n,p))


#Geometric Distribution Part 2


num_denom = list(map(int, input().split()))
n=int(input())
p= num_denom[0]/num_denom[1]

def g(n,p):
    ans=0
    for i in range(1, n+1):
        ans += (p) * (1-p)**(i-1)
    final_ans = round(ans,3)
    return final_ans

print(g(n,p))   