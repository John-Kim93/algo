import sys
L, C = map(int, sys.stdin.readline().split())
elements = sorted(sys.stdin.readline().split())
moem_list = ["a", "e", "i", "o", "u"]
result = set()


def bfs(now, moem_check, jaem_check, idx):
    if moem_check and jaem_check == 2 and len(now) == L:
        result.add(now)
        return
    if idx == C:
        return
    # 추가 안하고 다음
    bfs(now, moem_check, jaem_check, idx + 1)
    # 모음인지 체크
    n_char = elements[idx]
    if n_char in moem_list:
        if not moem_check:
            moem_check = 1
    else:
        if jaem_check < 2:
            jaem_check += 1
    # 추가 하고 다음
    bfs(now + n_char, moem_check, jaem_check, idx + 1)


for i in range(0, C - (L - 1)):
    # 인덱스별로 하나씩 넣고 출발 (마지막 2개는 최소 조건을 절대 충족하지 못함으로 C - 2까지만 본다.)
    if elements[i] in moem_list:
        bfs(elements[i], 1, 0, i + 1)
    else:
        bfs(elements[i], 0, 1, i + 1)

for ans in sorted(list(result)):
    print(ans)