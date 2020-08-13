def solution(clothes):
    answer = 1
    Dictionary={}
    for ele in clothes : 
        key = ele[1]
        value=ele[0]
        if key in Dictionary:
            Dictionary[key].append(value)
        else:
            Dictionary[key]=[value]
    for key in Dictionary.keys():
        answer = answer * (len(Dictionary[key])+1)
    return answer-1