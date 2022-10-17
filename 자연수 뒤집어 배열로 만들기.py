def solution(n):
    text = str(n)
    length = len(text)
    answer = []
    for i in range(length-1, -1, -1) :
        num = text[i]
        answer.append(int(num))
    return answer


def digit_reverse(n) :
    a = []

    while n>1 :
        a.append(int(n%10))
        n/=10

    return a
