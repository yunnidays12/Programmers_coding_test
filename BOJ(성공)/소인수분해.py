
n = int(input())

if n != 1 :
    d = 2
    the_list = []

    while True :

        if n < d : break

        if n%d != 0 :
            d += 1
        else :
            the_list.append(d)
            n = n//d

    for i in the_list : print(i)

else : print("")