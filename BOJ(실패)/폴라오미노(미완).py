
s = input()
con = 0
answer = ""

pointer = 0

while True :

    pointer += 1

    if pointer > len(s) : break

    if s[pointer] == "X" :
        con += 1

    else : 
        if con % 2 == 0 : answer += "B"*2
        elif con % 4 == 0 : answer += "A"*4
        else : 
            print(-1)
            break
        answer += "."

print(answer)