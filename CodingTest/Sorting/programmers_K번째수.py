def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_copy=array[commands[i][0]-1:commands[i][1]]
        array_copy.sort(key=None, reverse=False)
        answer.append(array_copy[commands[i][2]-1])
    return answer