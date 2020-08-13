import heapq
def solution(scoville, K):
    answer=0   
    heap=[]
    for i in scoville:
        heapq.heappush(heap, i)
    while(heap[0]<K):
        if len(heap)==1:
            answer=-1
            break
        else:
            n=heapq.heappop(heap)
            m=heapq.heappop(heap)
            heapq.heappush(heap,n+(m*2))
            answer+=1
    return answer