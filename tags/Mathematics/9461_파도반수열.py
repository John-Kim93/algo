import sys

arr = [0,1,1,1,2,2]
for i in range(1, 96):
    arr.append(arr[i] + arr[i+1] + arr[i+2])

T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    print(arr[N])