def solution(phone_number):
    phoneLen = len(phone_number)
    text = ""
    for i in range(phoneLen-4, phoneLen) :
        text += phone_number[i]
    return ("*" * (phoneLen-4)) + text
