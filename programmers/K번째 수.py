def solution(array, commands):
    answer = []
    tmp = []
    for n in range(len(commands)):
        tmp = []
        #i,j,k 지정
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        for m in range(i-1,j):
            tmp.append(array[m])
            print("="*20)
            tmp.sort()
            print(tmp)
        answer.append(tmp[k-1])
        # print(answer)
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

##다른 풀이

def solution2(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer
print(solution2(array, commands))