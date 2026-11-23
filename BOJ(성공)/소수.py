
prime_number = []

n = int(input())
m = int(input())

for i in range(n, m+1) :
    for j in range(2, int(i**0.5)+1) :
        if i%j == 0 : break
    else : 
        if i != 1 : prime_number.append(i)

if len(prime_number) != 0 :
    print(sum(prime_number))
    print(min(prime_number))

else : print(-1)