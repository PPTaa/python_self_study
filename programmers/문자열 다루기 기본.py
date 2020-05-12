## 문자열 다루기 기본
def solution(s):
    number = ['1','2','3','4','5','6','7','8','9','0']
    if len(s) != 4 and len(s) != 6:
        print("확인")
        answer = False
    else:
        for i in range(len(s)):
            if s[i] in number:
                answer = True
            else:
                answer = False
                break
    return answer
s1="a234"
s2="1234"
print(solution(s2))
##모범답안 ===========================
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)