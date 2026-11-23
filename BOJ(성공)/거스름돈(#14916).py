
n = int(input())

the_case = []

for k in range(0, (n//5)+1) :

    if (n-5*k) % 2 == 0 :
        t = (n-5*k) // 2
        the_case.append(k+t)

if len(the_case) != 0 :
    print(min(the_case))

else : print(-1)