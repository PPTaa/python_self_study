# 함수 미사용
a = int(input())
p=0
for n in range(a+1):
    p = n+p
    print(p)

print((a*(a+1)//2))

# 함수를 사용
def sum(n):
    e = n*(n+1)//2
    return e

print(sum(6))
