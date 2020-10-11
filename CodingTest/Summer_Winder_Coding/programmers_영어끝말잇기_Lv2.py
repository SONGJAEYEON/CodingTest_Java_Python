#n 끝말잇기에 참여하는 사람의 수
words=["hello", "one", "even", "never", "now", "world", "draw"] 
def solution(n, words):
    #n 끝말잇기에 참여하는 사람의 수 
    answer=[0,0]
    for i in range(1,len(words)):
        #이미 나왔던 단어를 말하는 경우 실패!
        if (words[i] in words[:i]) or (words[i-1][-1] != words[i][0]):
            answer[0]= (n if (i+1)%n==0 else (i+1)%n)
            answer[1]= i//n+1
            break
    return answer