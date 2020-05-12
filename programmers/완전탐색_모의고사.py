def solution(answers):
    no_1 = [1,2,3,4,5]
    no_2 = [2,1,2,3,2,4,2,5]
    no_3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    answer = []

    for i in range(len(answers)):
        if answers[i] == no_1[i%len(no_1)]:
            scores[0] += 1
        if answers[i] == no_2[i%len(no_2)]:
            scores[1] += 1
        if answers[i] == no_3[i%len(no_3)]:
            scores[2] += 1

    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
    return answer

answers = [1,2,3,4,5,1,3,5,4,2,3,1,4]
print(solution(answers))
## 다른 풀이 
def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        print(idx,s)
        if s == max(score):
            result.append(idx+1)

    return result

print(solution2(answers))