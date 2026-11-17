
money = int(input())
pay_money = 1000 - money

money_list = [500, 100, 50, 10, 5, 1]
cnt = 0
point = 0

while True :
    if pay_money == 0 : break

    if pay_money >= money_list[point] :
        pay_money -= money_list[point]
        cnt += 1

    else :
        point += 1

print(cnt)