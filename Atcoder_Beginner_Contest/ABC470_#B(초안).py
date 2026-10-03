
"""
[문제]
  1. n개의 공이 있고, 1번부터 n번까지의 색이 칠해져있다. (각 공의 색을 c_i라 한다.)
  2. 한 번의 연산으로, n개의 색 중에 아무거나로 바꿀 수 있다.
  3. 모든 공의 색을 같은 색으로 바꾸기 위한 최소한의 연산의 횟수를 출력하라.

[입력]
  1. 색의 수 n개 (100 이하의 자연수)
  2. i번째 공의 색 c_i

[아이디어]
  1. 가장 많은 공의 색 번호를 찾고,
  2. 나머지를 그 색 번호로 바꾸는 로직을 짜자.
"""

n = int(input())
c_list = list(map(int, input().split()))
number = [0 for _ in range(0, n+1)]

for i in c_list : number[i] += 1
most_number = max(number)

print(n - most_number)

# [실행결과] AC