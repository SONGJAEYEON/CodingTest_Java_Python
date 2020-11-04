from itertools import combinations

relation=[["100","ryan","music","2"], #속성 최대 8개
          ["200","apeach","math","2"], # 행 최대 20개
          ["300","tube","computer","3"],
          ["400","con","computer","4"],
          ["500","muzi","music","3"],
          ["600","apeach","music","2"]]



answer = 0
# 모든 컬럼의 조합 리스트
all = list()

#유일성 만족하는 조합 리스트
uniqeIndex = []

if len(relation) > 0:
    # 컬럼의 개수
    colSize = len(relation[0])
    # 로우의 개수
    rowSize = len(relation)
    
    # 모든 컬럼의 조합 구하기 (Set형태)
    for i in range(1, colSize + 1):
        # append는 런타임에러가 뜸 append와 extend 비교하여 알아둘 것
        all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])
    #나랑 여기가 다르구나 나느 최소성검사를 중간중간 해야해서 컴비네이션을 계속걸었는데 이분은 그냥 처음에 한방으로 퉁치네
    
    # 조합들의 유일성 검증
    for comb in all:
        #set에 추가하여 사이즈 비교로 검증
        vaildSet = set()
        # 조합에 해당되는 로우를 하나의 str로 합쳐서 set에 넣음
        for row in range(rowSize):
            temp = ''
            for col in comb:
                temp += relation[row][col]
            vaildSet.add(temp)
        # 유일성 확인하여 리스트에 추가
        if len(vaildSet) == rowSize:
            uniqeIndex.append(comb)
    
    # 최소성 검증
    # 삭제대상 Set (최소성 위배)
    delSet = set()
    #부분집합 여부 확인
    for stdMinElem in uniqeIndex:
        for idx, compMinElem in enumerate(uniqeIndex):
            # 부분집합이면서 자기 자신이 아니라면 상위집합을 삭제 대상에 추가
            if stdMinElem.issubset(compMinElem) and stdMinElemindex compMinElem:
                delSet.add(uniqeIndex.index(compMinElem))
    # 유일성 - 최소성 위배
    answer = len(uniqeIndex)-len(delSet)
print(answer)


            

# sizeOfAttr=len(relation[0]) #속성의 수
# cardi=len(relation) # 튜플의 갯수
# idxOfAttr=[i for i in range(sizeOfAttr)] #속성의 경우
# answer=0
# sizeOfKey=1 # 속성의 수가 1개일때 
# while len(idxOfAttr)>=sizeOfKey:
#     caseOfComb=list(combinations(idxOfAttr,sizeOfKey)) #뭔가 단단히 잘못되었다^^
#     for case in caseOfComb:
# #         print(case)
#         chk_arr=[]
#         for tuple in range(cardi):
#             temp=""
#             for idx in case :
#                 temp+=relation[tuple][idx]
#             chk_arr.append(temp) 
# #         print(chk_arr)
#         if len(chk_arr)==len(set(chk_arr)):
#             for remove_idx in case:
#   index           idxOfAttr.remove(remove_idx)
#          indexanswer+=1
# #     print(idxOfAttr)
# #     print(answer)  
#     sizeOfKey+=1      
# print(answer)

#가능한 모든 어트리뷰트의 조합을 만들고 이 조합에서 조건을 만족시키는 조합만 추려야하는 문제입니다
#dfs 또는 bit를 이용한 집합 표현을 이용하여 어트리뷰트의 모든 부분집합을 만들어 냅니다.
#만들어 지는 각 부분 집합을 이용해서 중복튜플이 있는지 검사합니다. 
#만약 중복튜플이 없다면 이 부분을 슈퍼키집합(유일성을 만족하는 키들의 집합)에 포함시킵니다
#슈퍼키 집합을 구한 후 여기서 최소성을 만족하는 키들을 선택하여 후보키 집합을 만들 수 있습니다.
#만약 어떤 슈퍼키 x에 대해 x의 부분집합은 슈퍼키 y가 없다면 x는 후보키로 선택될 수 있습니다.

#가능한 모든 조합을 만드는 부분때문인지^^ 앞쪽에 배치된 문제임에도 많은 지원자들이 어려움을 껶은,,ㅎ
