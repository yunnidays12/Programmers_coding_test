
#[조건1] A_i 번째 후추는 i번째 접시에만 뿌릴 수 있다.
#[조건2] i번째 접시에는 후추를 총 B_i그램까지 뿌릴 수 있다.
#[조건3] j번째 후추는 C_j 그램을 넘겨 뿌릴 수는 없다.
#[구하라는 것] 접시에 뿌릴 수 있는 최대 후추의 그램

#[입력변수] 
# 1. N, M (1 ≤ N, M ≤ 1000) : 접시의 수, 후추의 수

#[변경한 점] 
# a_b_list를 굳이 만들 필요 없이 그때그때 빼도 되는 것임.

n, m = map(int, input().split())
c_list = list(map(int, input().split()))
origin_sum = sum(c_list)

for i in range(n) :
    a, b = map(int, input().split())

    if c_list[a] != 0 :
        if c_list[a] <= b :
            c_list[a] = 0
        else : c_list[a] -= b

print(origin_sum - sum(c_list))

#[실행결과] AC