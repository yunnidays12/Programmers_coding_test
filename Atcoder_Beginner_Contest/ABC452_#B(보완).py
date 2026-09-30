
"""
[문제]
  1. 타카하시가 일하는 회사에는 N개의 직원과 M개의 부서가 있음. 직원과 부서는 서로 매칭되어있음.
  2. 현재 A_i번째 부서에서 일하는 중인데, 다음 분기때는 B_i로 이직할 예정.
  3. 각 부서별로 부서의 맴버의 변동을 각각 구하시오.

[입력] 다 100 이하의 변수
  1. 직원의 명수 N, 부서의 개수 M　(100 이하)
  2. 현재 직원의 부서 A_i, 다음 분기 직원의 부서 B_i

[수정할 점]
  1. 굳이 리스트를 두 개나 만들어야 할까? 하나만 만들어서 돌려쓰자!
"""

n, m = map(int, input().split())

move_list = [0] * (m+1)

for _ in range(n) :
    a, b = map(int, input().split())
    move_list[a] -= 1
    move_list[b] += 1

for i in range(1, m+1) :
  print(move_list[i])