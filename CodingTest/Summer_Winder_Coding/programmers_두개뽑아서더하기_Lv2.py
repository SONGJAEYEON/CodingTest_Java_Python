def solution(numbers):
    result_set=set()
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if i!=j:
                result_set.add(numbers[i]+numbers[j])
    answer=sorted(list(result_set))
    return answer