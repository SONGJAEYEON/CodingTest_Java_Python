# 문제 설명
# 쇼핑몰에서 고객들이 주문한 상품을 배송하려 합니다. 판매 중인 물품은 모두 n 종류이며, 각 상품별로 1부터 n까지 번호가 하나씩 붙어있습니다. 모든 고객은 각자 2 종류씩 상품을 주문했는데, 배송 효율성을 위해 2 종류 상품의 재고가 모두 남아있는 경우에만 배송하려 합니다. 이는 고객이 주문한 두 상품 중 하나라도 재고가 없다면 두 상품을 모두 배송하지 않는다는 의미입니다.
# 
# 예를 들어 어떤 고객이 [1번, 3번] 상품을 주문했고, 두 상품의 재고가 모두 남았다면 해당 상품을 고객에게 배송합니다. 만약, 또 다른 고객이 [3번, 5번] 물품을 주문했고, 3번 물품은 재고가 남았지만 5번 물품의 재고가 없다면 두 상품 모두 배송하지 않습니다.
# 
# 전체 상품 종류의 개수 n, 고객이 주문한 두 상품의 번호와 배송 여부가 담긴 2차원 배열 delivery가 매개변수로 주어집니다. 이때, 재고가 확실히 남은 상품은 'O', 재고가 확실히 없는 상품은 'X', 재고가 남았는지 모르는 상품은 '?'로 표시한 문자열을 return 하도록 solution 함수를 완성해주세요.
# 
# 제한사항
# n은 2 이상 1,000 이하인 자연수입니다.
# delivery의 행(세로) 길이는 1 이상 100,000 이하이고, 열(가로) 길이는 3입니다.
# delivery의 각 행은 [첫 번째 상품 번호, 두 번째 상품 번호, 배송 여부]를 의미합니다.
# 상품 번호는 1 이상 n 이하인 자연수입니다.
# 배송 여부는 0 또는 1이며, 0은 배송하지 않았다는 의미, 1은 배송했다는 의미입니다.
# 서로 다른 사람이 같은 상품을 주문했을 수 있으며, 배송 여부가 모순되는 경우는 없습니다.
# 첫 번째 상품 번호와 두 번째 상품 번호가 같은 경우는 없습니다.
# 재고가 남은 상품은 모든 고객에 배송되도록 충분한 양이 남았다고 가정합니다.
# 정답은 1번 상품부터 n번 상품까지 각 상품의 재고 여부를 순서대로 이어 붙인 문자열을 return 하면 됩니다.


# n    delivery    result
# 6    [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]    "O?O?X?"
# 7    [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]    "O?O?XXO"

# n=7
# delivery= [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]] 
# delivery.sort(key=lambda x:-x[2])
# answer=["?" for _ in range(n+1)]
# certain=[]
# for a,b,value in delivery:
#     if value==1:
#         answer[a]="O"
#         certain.append(a)
#         answer[b]="O"
#         certain.append(b)
#     else:
#         if a in certain:
#             answer[b]="X"
#         elif b in certain:
#             answer[a]="X"
# print("".join(answer[1:]))

# encrypted_text    key    rotation    result
# qyyigoptvfb    abcdefghijk    3    hellopython

# encrypted_text="qyyigoptvfb"

encrypted_text="optvfbqyyig"
rotation=-2
key="abcdefghijk"

# temp=encrypted_text[len(encrypted_text)-abs(rotation):]+encrypted_text[:len(encrypted_text)-abs(rotation)]
# print(temp)
def solution(encrypted_text, key, rotation):
    if rotation<0:
        temp=encrypted_text[len(encrypted_text)-abs(rotation):]+encrypted_text[:len(encrypted_text)-abs(rotation)]
    elif rotation>0:
        temp=encrypted_text[rotation:]+encrypted_text[:rotation]
    else:
        temp=encrypted_text
    for a,b in list(zip(temp,key)):
        if  ord(a)-(ord(b)-96)<96:
            print(chr(ord(a)-(ord(b)-96)+26),end="")
        else:
            print(chr(ord(a)-(ord(b)-96)),end="")
solution(encrypted_text, key, rotation)
#     return "".join(list(map(lambda a:chr(ord(a[0])-(ord(a[1])-96)+26) if ord(a[0])-(ord(a[1])-96)<96 else chr(ord(a[0])-(ord(a[1])-96)),list(zip(temp,key)))))

# v    answer
# [[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]    [2,1,2]
# [[0,0,1],[2,2,1],[0,0,0]]    [2,1,1]