import sys

input = sys.stdin.readline

number_list = []

n = int(input())

for _ in range(n) :
    input_num = int(input())
    number_list.append(input_num)

number_list.sort()

for i in number_list : print(i)