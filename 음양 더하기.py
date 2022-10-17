def solution(absolutes, signs):
    sum = 0
    for i in range(len(signs)) :
        if signs[i] == True :
            sum += absolutes[i]
        else :
            sum -= absolutes[i]
    return sum

def solution(absolutes, signs):
    return sum(absolutes[i] * (1 if signs[i] else -1) for i in range(len(signs)))
