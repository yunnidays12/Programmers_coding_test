
while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 : break

    n_set = set()
    m_set = set()

    for _ in range(n) :
        n_input = int(input())
        n_set.add(n_input)

    for _ in range(m) :
        m_input = int(input())
        m_set.add(m_input)

    answer = len(n_set&m_set)
    
    print(answer)