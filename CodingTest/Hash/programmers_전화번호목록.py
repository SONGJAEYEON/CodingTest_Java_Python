def solution(phone_book):
    sorted_List=sorted(phone_book,key=len)
    answer =True
    for phone in sorted_List : 
        sorted_List=sorted(sorted_List,key=len)
        str_short=":"+phone;
        sorted_List.remove(phone)
        str_long=":".join(sorted_List)
        if str_long.find(str_short)!=-1 :
            answer=False
            break;
        else:
            sorted_List.append(str_short)
    return answer