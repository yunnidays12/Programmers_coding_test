# [문제] 각 단어의 첫 글자에 따라 점수를 부여하고자 한다.
# [입력] 단어가 공백을 기준으로 들어온다.

score_dict = {
    2 : ["a", "b", "c"], 3 : ["d", "e", "f"],
    4 : ["g", "h", "i"], 5 : ["j", "k", "l"],
    6 : ["m", "n", "o"], 7 : ["p", "q", "r", "s"],
    8 : ["t", "u", "v"], 9 : ["w", "x", "y", "z"]
    }

n = int(input())
input_word = list(map(str, input().split()))
answer = ""

for word in input_word :
    for i in range(2, 10) :
        if word[0] in score_dict[i] :
            answer += str(i)
            break

print(answer)

#[출력결과] AC