def solution(num):
    x = 0
    while(x <= 500) :
        if num == 1 :
            return x
        else :
            x += 1
            if (num % 2 == 0) :
                num = num / 2
            else :
                num = (num * 3) + 1
    return -1
