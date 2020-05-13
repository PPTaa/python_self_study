def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        # print(arr[i])
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[len(arr)-1])
    return answer

arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]
arr3 = [1,1,1,3,3,3,4,4,4,8,8,8,8,2,2,2,2,2,2,3,3,3,3,3]
arr4 = [1,0,3,6,4,5,3,3,1,1,5]
print(solution(arr4))