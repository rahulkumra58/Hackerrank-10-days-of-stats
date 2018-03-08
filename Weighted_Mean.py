'''
Input Format

5
10 40 30 50 20
1 2 3 4 5

Output Format

32.0
'''

N= int(input())
num = list(map(int, input().split()))
weights = list(map(int, input().split()))
sunm=0
weightss=0
for a,b in zip(num,weights):
    sunm+=a*b
    weightss+= b
final_sum=sunm/weightss
print(round(final_sum,1))
