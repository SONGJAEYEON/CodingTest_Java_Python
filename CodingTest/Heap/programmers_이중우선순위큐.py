import heapq as hq

def solution(operations):
    heap=[]
    for oper in operations:
        if oper[0]=="I":
            hq.heappush(heap,int(oper.split("I ")[1]))
        elif oper=="D -1" and len(heap)!=0:
            hq.heappop(heap)
        elif oper=="D 1" and len(heap)!=0:
            hq._heappop_max(heap)
    return([max(heap),min(heap)] if len(heap)!=0 else [0,0])