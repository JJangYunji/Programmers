def solution(x):

    answer = x % sum(int(i) for i in str(x)) == 0
    
    return answer


def Harshad(n) :
    return n % sum([int(c) for c in str(n)]) == 0
