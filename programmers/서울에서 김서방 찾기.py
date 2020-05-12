def solution(seoul):
    Kim = "Kim"
    print(seoul.index(Kim))
    answer = ""
    for i in range(len(seoul)): 
        print(seoul[i])
        if seoul[i] == Kim:
            answer =f"김서방은 {i}에 있다"
    return answer

seoul = ["J","a","ne","Kim"]
print(solution(seoul))

## 모범 답안
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))