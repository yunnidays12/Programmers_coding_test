
n, m = map(int, input().split())

cd_dict = {}

for _ in range(n) :
    n_input = int(input())
    cd_dict[n_input] = 1

for _ in range(m) :
    m_input = int(input())
    if m_input not in cd_dict :
        cd_dict[m_input] = 1
    else : cd_dict[m_input] += 1

for _ in range(1) :
    last_input = input()

answer = 0

for i in cd_dict :
    if cd_dict[i]%2 == 0 : answer += 1

print(answer)