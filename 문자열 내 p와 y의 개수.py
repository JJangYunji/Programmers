def solution(s):
    answer = True
    p = 0
    y = 0
    sLen = len(s)
    for i in range(sLen) :
        if s[i].lower() == 'p' :
            p += 1
        elif s[i].lower() == 'y' :
            y += 1
    if p == y :
        answer = True
    elif p == 0 and y == 0 :
        answer = True
    else :
        answer = False
    return answer

def numPY(s) :
    return s.lower().count('p') == s.lower().count('y')
