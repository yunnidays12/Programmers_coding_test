
"""
[문제]
  1. 대소문자 구분없이, 같은평 중 최댓값을 출력하라.
  2. 예를 들어, AtCoder, ATCODER, atcoder은 모두 같은 평가이다.

[입력]
  1. 사람의 명수를 나타내는 변수 n (100 이하)
  2. 각 사람의 평가가 담긴 변수 S_i (각 길이는 10글자 이하)

"""

n = int(input())
progress_db = {}

for _ in range(n) :
    user_input = input().lower()
    if user_input not in progress_db :
        progress_db[user_input] = 1
    else : progress_db[user_input] += 1

print(max(progress_db.values()))