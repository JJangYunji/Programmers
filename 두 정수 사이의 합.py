def solution(a, b):
    sum = 0
    if a == b :
        return a
    elif a < b:
        for i in range(a, b+1) :
            sum += i
    else :
        for i in range(a,b-1,-1) :
            sum += i
    return sum


def adder(a,b) :
    return sum(range(min(a,b),max(a,b)+1))
