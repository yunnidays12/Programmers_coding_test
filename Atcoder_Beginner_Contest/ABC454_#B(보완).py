
"""
[문제]
  1. 센서는 0초부터 t초까지 다음 규칙에 의해 데이터를 읽는다.
    - 0초일 때는, 데이터를 저장한다.
    - (1초부터 t초까지의 데이터) i초와 i+1초의 데이터의 차의 절대값이 X 이상이어야 한다.
  2. i초 때 센서가 읽은 데이터를 A_i라 할 때, 시간이 흐름에 따라 저장된 데이터를 출력하라.

[입력]
  1. 전체 시간을 의미하는 변수 t (100 이하)
  2. 절대값의 최솟값을 의미하는 변수 x (100 이하)
  3. 각 시간때마다의 데이터 A_i (100 이하)

[수정할 점]
  1. 리스트를 만들지 말고, 저장된 전 데이터만 알면 구할 수 있잖아.
  2. 0번째는 항상 출력하게 만들면 되지.

"""

t, x = map(int, input().split())
time_data = list(map(int, input().split()))

before_data = time_data[0]
print("0" + " " + str(before_data))

for i in range(1, t+1) :
  if abs(time_data[i] - before_data) >= x :
    print(str(i)+" "+str(time_data[i]))
    before_data = time_data[i]

# [실행결과] AC