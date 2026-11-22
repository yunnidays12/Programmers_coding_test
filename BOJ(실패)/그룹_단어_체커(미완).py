
t = int(input())
answer = 0

for _ in range(t) :
    s = input()
    char_dict = {}

    for i in range(1, len(s)) :
        if s[i] not in char_dict :
            char_dict[s[i]] = 1
        else :
            if char_dict[s[i]] != 0 :
                if s[i] == s[i-1] :
                    char_dict[s[i]] -= 1
                else :
                    print("No!")
                    break

    else : print("Yes!")
