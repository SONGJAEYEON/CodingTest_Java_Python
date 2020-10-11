skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]

answer = 0
for tree in skill_trees:
    current_tree_skill = [char for char in tree if char in skill]
    print(current_tree_skill)
    possibility = True
    for i, j in zip(current_tree_skill, skill):
        if i != j:
            possibility = False
            break
    if possibility:
        answer += 1
print(answer)

# skill_case=[ skill[:i] for i in range(1,len(skill)+1)]
# print(skill_case)
# cnt=0
# for tree in skill_trees:
#     skill_str="".join(list(filter(lambda x: x in skill,tree)))
#     if skill_str in skill_case:
#         print(skill_str)
#         cnt+=1
# print(cnt)
        
#스킬트리에 주어진 조건의 스킬들이 하나도 없어도 정답으로,,!
    