import sys

arr = [1] * ((123456 * 2) + 1)
for i in range(2, 123456):
    num = 2 * i
    # 탐색 최적화 (2의 배수 탐색 생략)
    if i != 2 and i % 2 == 0:
        continue
    # 에레스토테네스의 채 적용
    while num <= 123456 * 2:
        arr[num] = 0
        num += i

while True:
    n = int(sys.stdin.readline())
    # 0이 주어진 경우 종료
    if not n: break
    # 채로 걸러진 소수 값 탐색 및 카운트
    cnt = 0
    for i in range(n + 1, 2*n + 1):
        if arr[i]:
            cnt += 1
    print(cnt)