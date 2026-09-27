"""
[문제]
  1. 각 나무꾼은 1,2,...,N은 각 도끼를 연못에 빠뜨림
  2. i번째 나무꾼이 "A_i번째 도끼 소유자임."이라고 함.
  3. 동시에 연못의 신은 i번째 도끼가 B_i번째 나무꾼의 것인 걸 알음.
  4. 모든 나무꾼이 진실이라면 Yes, 아니면 No를 출력하라.

[입력]
  [첫번째 줄] 나무꾼 명수 : N (100명 이하)
  [두번째 줄] 인덱스가 i면, i번째 나무꾼이 소유한 도끼번호 A_i (N개)
  [세번째 줄] 인덱스가 i면, i번째 도끼의 주인인 나무꾼의 번호 B_i (N개)
  
"""

n = int(input())
A_i = list(map(int, input().split()))
B_i = list(map(int, input().split()))
is_truth = 1

for i in range(0, n) :
    if A_i[B_i[i]-1] != i+1 :
        is_truth = 0
        break

if is_truth == 1 : print("Yes")
else : print("No")

#[실행결과] AC