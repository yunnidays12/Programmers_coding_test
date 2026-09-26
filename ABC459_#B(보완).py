# [문제] 각 단어의 첫 글자에 따라 점수를 부여하고자 한다.
# [입력] 단어가 공백을 기준으로 들어온다.

# [보완할 점] 
# 1. 굳이 딕셔너리 안에 리스트로 만들지 말고, 문자열로 두기
# 2. 굳이 list(map(...)) 안써도 되는 거 알면서 왜 그럼?

score_dict = {
    2 : "abc" , 3 : "def", 4 : "ghi", 5 : "jkl",
    6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"
    }

n = int(input())
input_word = input().split()
answer = ""

for word in input_word :
    for i in range(2, 10) :
        if word[0] in score_dict[i] :
            answer += str(i)
            break

print(answer)

#[출력결과] AC