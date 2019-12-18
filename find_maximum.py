#값들 중에서 최대 값 찾기
def max_test(a):
    n = len(a)
    max_num = 0
    for i in range(n):
        if a[i]>max_num:
            max_num=a[i]
    return max_num

#그 최댓값의 인덱스 찾기
def max_test_idx(b):
    m=len(b)
    max_num_idx = 0
    for i in range(m):
        if b[i] > b[max_num_idx]:
            max_num_idx = i
    return max_num_idx

l=[999,1,2,6,7,5,99999999999999999,3,8,6,9,4,10,4,654,54,984,5,5314654,4,5,13,1231,54,51,31,58,64,6454513]
print(max_test(l))
print(max_test_idx(l))

