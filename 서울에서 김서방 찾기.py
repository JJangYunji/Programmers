def solution(seoul):
    return ('김서방은 %d에 있다' % seoul.index('Kim'))


def solution(seoul) :
    for i in range(len(seoul)) :
        if seoul[i] == "Kim" :
            return "김서방은" + " " + str(i) + "에 있다"
    return answer
