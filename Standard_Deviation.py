'''

Input Format
5
10 40 30 50 20

Output Format

14.1

'''





N = int(input())
numbers = sorted(list(map(int, input().split())))
mean1= sum(numbers)/N
final_sum=0

for i in numbers:
    x=(i-mean1)**2
    final_sum+=x
    SD= (final_sum/N)**(1/2)
print(round(SD,1))
