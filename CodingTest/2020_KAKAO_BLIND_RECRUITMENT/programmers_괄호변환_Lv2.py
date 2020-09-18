#( 와  ) 만으로 이루어진 문자열이 있을 경우 (의 개수와 )의 개수가 같다면 이를 균형잡힌 괄호열이라고 부릅니다

# (와 )의 짝이 맞다면 이를 올바른 괄호 문자열이라고 부릅니다

# ( 와 )로만 이루어진 문자열이 균형잡힌 괄호문자열이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다

# 1. 입력이 빈 문자열인 경우 빈 문자열을 반환합니다 

# 2. 문자열 w을 두 균형잡힌 괄호 문자열 u  v로 분리합니다. 단 u는 균형잡힌 괄호문자열로 더이상 분리할 수 없어야 하며 v는 빈 문자열이 될 수 있습니다.

# 3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행합니다

#3-1 수행한 결과 문자열을 u에 이어붙인 후 반환합니다. 끄읏!

# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 

#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 

#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 

#   4-3. ')'를 다시 붙입니다. 

#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 

#   4-5. 생성된 문자열을 반환합니다.

# p    result
# "(()())()"    "(()())()"
# ")("    "()"
# "()))((()"    "()(())()"

p="()))((()"


# 1. u, v로 분리 (여기서는 v를 p로 했음 -> v로 바꿔주면 while문에서 못빠져나옴)
# 올바른 문자열인지 췍
def check(p):
    stack = []
    try:
        for i in p:
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
        return True
    except:
        return False 
# u, v로 나누기
def divide(p):
    count = [0, 0]
    for i in p:
        if i == '(':
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            break
    return p[:sum(count)], p[sum(count):]#,,,?
# 괄호 방향 뒤집어주기
def convert(u):
    temp = ''
    for i in u:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp
# 2. u가 올바른 문자열인지 체크하고 맞으면 answer에 붙여주고 아니면 재귀적으로 수행
def solution(p):
    answer = ''

    while len(p) != 0:
        u, p = divide(p)
        if check(u):
            answer += u
        else:
            answer += '(' + solution(p) + ')' + convert(u[1:-1])
            break

    return answer
# 2-1. answer에 '(' + v를 1번부터 재귀적으로 수행한 결과 + ')' + u의 앞뒤빼고 뒤집은 문자열을 붙인다.