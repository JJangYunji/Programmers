def solution(arr):
    sum = 0
    answer = 0
    for i in range(len(arr)) :
        sum += arr[i]
    answer = sum/len(arr)
    return answer
