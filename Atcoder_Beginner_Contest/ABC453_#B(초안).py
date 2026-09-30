
"""
[문제]
  1. H개의 행과 W개의 열이 열이 있다.
  2. 타카하시는 각 칸을 검정이나 하양으로 칠하려고 한다.
  3. 테두리는 다 검은색, 나머지는 하얀색으로 칠칠하려고 한다.
  4. 다 칠하고 나서서의 표를 출력하라. (검은색 #, 하얀색 .)
  5. 문제에서 말하는 더 세부적인 조건은 다음과 같다.
    - 두 점 (i,j)와 (k,l)에 대해, abs(i-k) + abs(j-l) = 1일때만 테두리에 인접했다 한다.
    - (i,j)가 테두리가 되기 위한 필요충분조건은, 인접한 테두두리가 많아야 3개일 때이다.

[입력]
  1. 표의 행의개수 H와, 열의　개수 W　(10이하)
"""

h, w = map(int, input().split())
answer_map = ["" for i in range(0, h)]

for i in range(0, h) :
  if i == 0 or i == h-1 :
    answer_map[i] += "#" * w

  else :
    for j in range(0, w) :
      if j == 0 or j == w-1 :
        answer_map[i] += "#"
      else : answer_map[i] += "."

for row in answer_map :
  print(row)
