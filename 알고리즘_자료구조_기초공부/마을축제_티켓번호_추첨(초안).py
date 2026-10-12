
number_dict = {}

n = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

for i in number_list :
    if i not in number_dict :
        number_dict[i] = 1
    else : number_dict[i] += 1

for i in number_dict :
    print(f"{i} {number_dict[i]}")