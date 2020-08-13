def solution(genres, plays):
    answer = []
    music={}
    sum={}
    for i in range(len(genres)):
        key=genres[i]
        value=plays[i]
        if key in music.keys():
            sum[key]+=value
            music[key].append([value,i]) 
        else:
            sum[key]=value
            music[key]=[[value,i]]
    order = []
    for key in music.keys():
        order.append([key,sum[key]])
    order.sort(key=lambda x:x[1],reverse=True)
    compare=[]
    for i in range(len(order)):
        for j in range(0,2):
            try:
                play = music[order[i][0]]
                play.sort(key=lambda x:x[0],reverse=True)
                answer.append(play[j][1])
            except:
                continue
    return answer