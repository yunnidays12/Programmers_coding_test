
"""
[문제]
  1. n개의 공이 있고, 1번부터 n번까지의 색이 칠해져있다. (각 공의 색을 c_i라 한다.)
  2. 한 번의 연산으로, n개의 색 중에 아무거나로 바꿀 수 있다.
  3. 모든 공의 색을 같은 색으로 바꾸기 위한 최소한의 연산의 횟수를 출력하라.

[입력]
  1. 색의 수 n개 (100 이하의 자연수)
  2. i번째 공의 색 c_i

[수정할 점]
  1. counter 모듈을 써보는 것도 좋음.
"""

from collections import Counter

n = int(input())
c_list = list(map(int, input().split()))

print(n - max(Counter(c_list).values()))

# [실행결과] AC