#값들 중에서 최소 값 찾기
def min_test(a):
    n = len(a)
    min = a[0]
    for i in range(n):
        if a[i] < min:
            min = a[i]
    return min

#그 최소값의 인덱스 찾기
def min_test_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

l=[999,14,654,54,984,5,5314654,4,5,13,1231,54,51,31,58,64,6454513]
print(min_test(l))
print(min_test_idx(l))