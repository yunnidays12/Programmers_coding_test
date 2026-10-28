
"""
[문제]
  1. 길이가 n이고 영어 소문자로 구성된 문장 s와 t, 그리고 m개의 정수의 쌍 (L1, R1), (L2, R2), ... , (LM, RM)이 주어진다.
  2. 정수 i = 1,2,...,m에 대하여, 다음 조건을 만족하는 연산을 하려고 한다.
    - s의 Li부터 Ri까지의 문자열을 t의 Li부터 Ri까지의 문자열로 바꿀 것.
  3. m번의 연산이 끝나고나서의 s의 문자열을 출력하라.

[입력]
  1. 문자열 s와 t의 길이를 담는 변수 n (500,000 이하)
  2. 정수의 쌍의 개수를 담는 변수 m (200,000 이하)
  3. 1 <= Li <= Ri <= n

[시간복잡도] m * (s의 길이) * (t의 길이) = m*(n**2) --> 절대 불가.
            O(nlogn)나 O(n)으로 끝내는 것을 목표로 하기.
"""

n, m = map(int, input().split())
s = input()
t = input()

prefix_val = [0] * (n+1)

for _ in range(m) :
    l, r = map(int, input().split())
    prefix_val[l-1] += 1
    prefix_val[r] -= 1

for i in range(n) :
    prefix_val[i+1] += prefix_val[i]

answer = [s[i] if prefix_val[i]%2==0 else t[i] for i in range(n)]

print("".join(answer))