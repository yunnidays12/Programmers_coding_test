
num_list = [0]*101

n = int(input())
number_list = list(map(int, input().split()))

for i in number_list : num_list[i] += 1

for i in range(0, n) :
    if num_list[number_list[i]] != 0 :
        print(f"{number_list[i]} {num_list[number_list[i]]}")
