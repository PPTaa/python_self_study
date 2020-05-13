def solution(s, n):
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet2 = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for i in s:
        print(i)
        if alphabet1.find(i) != -1:
            num = alphabet1.find(i)+n
            if num > len(alphabet1)-1:
                num = num%26
                answer += alphabet1[num]
            else:
                answer += alphabet1[num]
        elif alphabet2.find(i) != -1:
            num = alphabet2.find(i)+n
            if num > len(alphabet2)-1:
                num = num%26
                answer += alphabet2[num]
            else:
                answer += alphabet2[num]
        else:
            answer += " "
    return answer
s = "Z X FV ZX"
n=1
print(solution(s,n))    

## 다른 풀이
def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
        print(result)
    return "".join(result) 
print(caesar("asd zSD Ax  zc ",1))