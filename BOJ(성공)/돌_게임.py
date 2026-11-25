
the_game = [-1, 0, 1, 0]

for i in range(4, 1001) :
    if the_game[i-1] == 0 :
        state1 = 1
    else : state1 = 0

    if the_game[i-3] == 1 :
        state2 = 0
    else : state2 = 1

    if state1 == state2 : the_game.append(state1)

n = int(input())

print("SK" if the_game[n] == 0 else "CY")