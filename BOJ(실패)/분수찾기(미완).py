
while True :
    n = int(input())

    if n == 0 : break

    line = 0

    #1. n번째가 몇번째 줄에 위치하는 지를 찾아야 한다.
    while True :
        if n <= 1 : break
        else :
            n -= line
            line += 1

    if n != 1 : n += line

    if line % 2 == 0 :
        under = line - abs(n) + 1
        upper = abs(n)

    else : 
        under = abs(n) + 1
        upper = line - abs(n) + 1

    print(n)
    print(f"{upper}/{under}")
