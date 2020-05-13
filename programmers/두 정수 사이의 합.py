def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a,b+1):
            answer += i
    else:
        for i in range(b,a+1):
            answer += i
    return answer
print(solution(10000000,3))

##다른 풀이1
def solution2(a,b):
    return sum(range(min(a,b),max(a,b)+1))
print(solution2(10000000,3))
##다른 풀이2
def solution(a, b):
    if a > b: 
        a, b = b, a
        print(a,b)
    return sum(range(a,b+1))
print(solution(10000000,3))