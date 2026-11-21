
def factorial(n) :
    if n == 0 : return 1
    else : return n * factorial(n-1)

def combination(n, m) :
    분자 = 1

    for i in range(n, n-m, -1) :
        분자 *= i

    return 분자 // factorial(m)

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    print(combination(m, n))