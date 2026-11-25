
n = int(input())
stu_list = []

for _ in range(n) :
    the_command = input().split()
    name = the_command[0]
    day = int(the_command[1])
    month = int(the_command[2])
    year = int(the_command[3])
    stu_list.append([name, year, month, day])

clean_data = sorted(stu_list, key = lambda x : (x[1], x[2], x[3]), reverse=True)

print(clean_data[0][0])
print(clean_data[-1][0])