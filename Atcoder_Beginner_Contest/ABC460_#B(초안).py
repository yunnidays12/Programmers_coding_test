
# [문제]
# 1. xy평면에 원 c_1, c_2가 있다. 각 중심의 좌표는 x1, y1 / x2, y2
# 2. 두 원이 서로 교점을 갖는지를 판별하라. (접하는 경우도 생각.)

# [입력조건]
# 1. 테스트 케이스의 수가 주어진다. (t)
# 2. 그리고 각 테스트 케이스의 입력은 다음과 같다.
# [입력] x1 y1 r1 x2 y2 r2

t = int(input())

for _ in range(t) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if r1+r2 >= distance :
        print("Yes")
    else :
        print("No")

#[실행결과] WA