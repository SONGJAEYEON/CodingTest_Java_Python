tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]


import heapq

heap=[]
arrive=["ICN"]
tickets.sort()
for ticket in tickets:
    heapq.heappush(heap,ticket)
while(len(heap)>0):
    for i in range(len(heap)):
        if heap[i][0]==arrive[-1]: #아마 이렇게 일일이 대조하는게 시간이 많이걸릴거같아유,,, 
            arrive.append(heap[i][1])
            heap.remove(heap[i])
            break
        else:
            i+=1
print(arrive)
      
# while(len(tickets)>0):
#     for i in range(len(tickets)):
#         if tickets[i][0]==begin: #아마 이렇게 일일이 대조하는게 시간이 많이걸릴거같아유,,, 
#             arrive.append(begin)
#             begin=tickets[i][1]
#             if len(tickets)==1:arrive.append(begin)
#             tickets.remove(tickets[i])
#             break
#         else:
#             i+=1
# print(arrive)
# [ICN, ATL, ICN, SFO, ATL, SFO]

# 사설도박장 19:37 
# ◽폐병원 22:18 10시,,,
# ◽유전자은행 1:02 
# ◽악령감옥 3:03 
# ◽벙커 6:11 아침6시네
# ◽태양여고 8:47
#  ◽스페셜 11:29
 


