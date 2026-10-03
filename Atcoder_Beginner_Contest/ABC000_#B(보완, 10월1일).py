"""
[문제]
  1. n명의 사람이 11번부터 n번까지 있다.
  2. 그리고 옷의 타입도 11부터 m까지 있다.
  3. 다음 질문에 yes 또는 no로 답해해라.
    - n명의 사람은 모두 다른 타입의 옷을 입고 있는가?
    - m개의 옷 타입은 적어도 한 번씩은 다 입혀졌는가?

[입력]
  1. 사람의 명수수를 담는 변수 n (100 이하)
  2. 옷 타입의 개수를 담는 변수 m (100 이하)
  3. i번째 사람이 입고 있는 옷 타입 f_i

[보완할 점]
  1. set_clothes 는 set(f_list)랑 (1,2,3,...,m)랑 같은지 확인만 하면 됌.
  2. 이렇게 되면 중복되는 지 체크하는 로직은 하나라도 겹치면 바로 break
"""

n, m = map(int, input().split())
f_list = list(map(int, input().split()))

last_clothes = []
set_clothes = set(f_list)

for i in range(0, n) :
  if f_list[i] in last_clothes :
    print("No")
    break
  else : last_clothes.append(f_list[i])

else : print("Yes")

if set_clothes == set(i for i in range(1, m+1)) :
  print("Yes")
else : print("No")

# [실행결과] AC
