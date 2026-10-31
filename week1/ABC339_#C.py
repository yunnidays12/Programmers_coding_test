
"""
[문제]
  1. 버스 탑승객들에게는 항상 음이 아닌 정수 번호가 주어진다.
  2. 버스에는 항상 0명 또는 더 많은 승객이 탑승해있으며, 출발한 후 n번 멈춘다.
  3. i번째 정차에서, 승객은 A_i명 증가한다. (음수도 가능)
  4. 또한, 정차하는 곳이 아닐 때에는 승객은 증감하지 않는다.
  5. n번의 증감정보가 주어질 때, 현재의 최소 승객은 몇 명인지 구하라.

[입력]
  1. 몇 번 멈출지 알려주는 변수 n (20만 이하)
  2. i번째 승강장에서 증감하는 승객의 수 A_i (-10억부터 10억까지)
"""

n = int(input())
a_list = [0] + list(map(int, input().split()))

prefix_sum = [0]
for i in range(1, n+1) :
    prefix_sum.append(a_list[i] + prefix_sum[i-1])

add_people = [0]

for i in range(1, n+1) :
    if prefix_sum[i] < 0 :
        add_people.append(abs(prefix_sum[i]))

print(prefix_sum[-1] + max(add_people))