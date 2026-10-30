
"""
[문제]
    1. 정수 N과 길이가 N인 수열 S가 주어진다.
    2. 정수 k에 대하여 다음을 만족하는 길이가 N인 수열 A를 찾아라.
      - A1+A2+...+AN = SK
"""

n = int(input())
s = [0] + list(map(int, input().split()))

reverse_sum = [0]
for i in range(1, n+1) :
    reverse_sum.append(s[i] - s[i-1])

answer = ""
for i in reverse_sum[1:] :
    answer += str(i) + " "

print(answer.strip())