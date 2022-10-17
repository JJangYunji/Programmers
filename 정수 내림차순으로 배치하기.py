def solution(n):
    aList = list(str(n))
    aList.sort(reverse=True)
    num = int("".join(aList))
    return num
