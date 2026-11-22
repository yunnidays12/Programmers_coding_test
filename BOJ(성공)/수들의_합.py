
"""
[아이디어] 
- 서로 다른 n개의 자연수의 합이 s. : s = a_1 + a_2 + ... + a_n
- 근데 최댓값을 구하라고 하면... 가장 작은 수부터 더해가야 한다.
- 1부터 더해나간다.
- i번째부터 j번째까지의 수의 합 : j(j+1)/2 - i(i-1)/2 = 200
"""

s = int(input())
total = 0
cnt = 0

for i in range(1, s+1) :
    if i*(i+1) < 2*s :
       cnt += 1
    
    else :
        total = i*(i+1)
        break

if total > 2*s : print(cnt)
else : print(cnt+1)
        