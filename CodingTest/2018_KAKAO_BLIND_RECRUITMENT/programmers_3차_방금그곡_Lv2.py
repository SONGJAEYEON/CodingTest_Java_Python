def convert(melody): 
    if "A#" in melody:melody=melody.replace("A#",'a')
    if "C#" in melody:melody=melody.replace("C#",'c')
    if "D#" in melody:melody=melody.replace("D#",'d')
    if "F#" in melody:melody=melody.replace("F#",'f')
    if "G#" in melody:melody=melody.replace("G#",'g')
    return melody
 
def solution(m,musicinfos):
    m=convert(m)
    answer=('(None)',None)
    for info in musicinfos:
        start,end,title,melody=info.split(",")
        start_h,start_m,end_h,end_m=map(int,start.split(":")+end.split(":"))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = convert(melody)
        melody_played = (melody*time)[:time] #아니도대체 어떻게 이렇게 코드가 짜지는거지,,,?
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):#와... 선생님 정말 코드가 정말 우아하시네여,,,
                answer = (title, time)
    return answer[0]  


