def solution(s):
    
    s=s.lower()
    answer = True
    
    countp = s.count("p")
    county = s.count("y")
    
    if countp == county:
        answer = True
    else:
        answer = False    
    print(countp, county)
    return answer

s1="pPoooyY"
s2="Pyy"
print(solution(s1))