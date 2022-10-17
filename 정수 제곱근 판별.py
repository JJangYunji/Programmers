import math

def solution(n):
    answer = 0
    x = int(math.sqrt(n))
    if (x%1==0):
        answer = (x+1)**2
    else :
        answer = -1
    return answer


def nextSqure(n) :
    sqrt = n ** (1/2)

    if sqrt % 1 == 0 :
        return(sqrt + 1) ** 2

    return 'no'
