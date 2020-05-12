def solution1(s):
    sorted(s,reverse=True)
    answer = ''.join(sorted(s,reverse=True))
    return answer

s="ZbcgdVeqscfg"
print(solution1(s))

#다른풀이

def solution2(s):
    lst = list(s)
    lst.sort()
    lst.reverse()
    print(lst)
    answer = "".join(lst)
    return answer

print(solution2(s))