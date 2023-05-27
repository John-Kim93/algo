import sys

M, N = map(int, sys.stdin.readline().split())
arr = [0] * (N + 1)
arr[0] = 1
arr[1] = 1

for i in range(2, N):
    now = i + i
    while True:
        if now > N:
            break
        arr[now] = 1
        now += i

for i in range(M, len(arr)):
    if not arr[i]:
        print(i)

