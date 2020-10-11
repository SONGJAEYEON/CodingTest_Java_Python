#위상정렬의 조건
#주어진 그래프에서 위상정렬을 하려면 아래와 같은 조건을 만족하는 그래프여야 한다

#위상정렬을 할 그래프는 간선이 방향성을 가지는 유향 그래프 여야 한다
# 그래프 내부에 순환이 있으면 안된다

"""
인접 행렬에서 본 그래프와 같은 모양의 그래프를 예로 들 것.
입력: 그래프의 인접 리스트
출력: 위상 정렬의 순서(같은 순서일 경우 아무거나 뽑음)
알고리즘
    1. 모든 정점의 진입 차수를 계산
    2. 진입 차수가 0인 정점을 스택에 삽입
    3. 위상 순서를 생성
https://sexy-developer.tistory.com/56?category=882923
"""
adj_list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}


def topological_sort_stack(adj_list):
    stack = []
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1

    print("in_degree 배열: ", in_degree)

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            stack.append(i)

    print("초기 스택: ", stack)
    while stack:
        node = stack.pop()
        answer.append(node)
        print("pop 된 노드: ", node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                stack.append(idx)

    print("answer: ", answer)


# print(topological_sort_stack(adj_list))

"""
이 아래에는 스택이 아닌 큐를 이용해서 위상 정렬을 해보겠다. 
"""

def topological_sort_queue(adj_list):
    import queue

    myQue = queue.Queue()
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1
    print("in_degree 배열: ", in_degree) # 그래 여기까진 똑같애

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            myQue.put(i) # 그래 여기까지도 똑같애 queue에 넣는거니까!! 

    print("초기 스택: ", myQue)
    while not myQue.empty(): #queue가 비어있지않다면 반복문 계속 실행!
        node = myQue.get() #맨앞에있는거 가져오고( 그럼 0이 빠지겠지맨첨엔??)
        answer.append(node)
        print("pop 된 노드: ", node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                myQue.put(idx)

    print("answer: ", answer)


# print(topological_sort_queue(adj_list))

# 응용1: 큐를 통해 동일한 위상 지니는 노드는 하나의 배열로 묶어서 출력하는 코드
# queue를 사용하는 경우 같은 위상의 순서를 가진 노드를 추출할 수 있다.

adj_list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}


def queue_topo_sort(adj_list):
    queue = []
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1
    print("in_degree 배열: ", in_degree)

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i) #그래 여기까진 똑같애 

    print("초기 큐: ", queue, "에서 반복 시작")
    while queue:
        print("\nqueue: ", queue)
        answer.append(queue)

        new_arr = []
        for i in queue:
            print(i, "에서 탐색 시작")
            for j in range(len(adj_list[i])):
                idx = adj_list[i][j] #리스트인데 이렇게 표기하는거 개멋있네 이렇게도할수있구나,,
                in_degree[idx] -= 1
                if in_degree[idx] == 0:
                    print("진입차수가 0이 된 정점: ", idx)
                    new_arr.append(idx)

        queue = new_arr

    print("answer: ", answer)


queue_topo_sort(adj_list)
