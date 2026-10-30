
"""
[문제]
  1. 타카하시는 n일 기차 여행을 계획중에 있다. 
  2. 각 일차에는 정규 비용을 내거나 아니면 하루 패스를 살 수 있다.
  3. i일차의 정규비용은 F_i엔이고, D개의 일일 패스는 P엔이다.
    - 발권된 D개의 패스권은 D번 언제든지 쓸 수 있고, 남겨도 상관없다.
  4. n일간의 기차여행의 최소값을 구하여라.

[입력]
  1. 며칠간의 여행인지를 알려주는 변수 n (20만 이하)
  2. 하루 패스를 파는 묶음 단위의 변수 d (20만 이하)
  3. 일일 패스를 d개씩 팔 때의 가격인 변수 p (10억 이하)
  4. i일차의 정규 비용의 변수 f_i (10억 이하)

[아이디어] (해설지 봄)
  1. 어떤 고정된 숫자 k가 있어서, kd >= n이면 일일 패스권만 사도 됌.
  2. 이때, 가장 적게 패스권을 사고 싶다면 k는 (n/d)보다 크면서 가장 가까운 정수이면 됌.
  3. 반대로, kd < n이면, f_i가 오름차순으로 정렬되있어서, (f'1, f'2, ... , f'n)라 되어있다면,
     1번부터 (n-kd)번까지의 인덱스의 요금들만 더하고, 패스권 가격을 더하면 됌.
"""

n, d, p = map(int, input().split())
F_cost = sorted(map(int, input().split()))

prefix_sum = [0]
for x in F_cost:
    prefix_sum.append(prefix_sum[-1] + x)

answer = float('inf')

for k in range((n - 1 + d - 1) // d + 1):
    cost = k * p + prefix_sum[max(0, n - 1 - k * d)]
    answer = min(answer, cost)

print(answer)