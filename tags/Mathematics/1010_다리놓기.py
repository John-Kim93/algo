'''
M개 중에서 N개를 조합하는 경우의 수를 구하는 문제이다.
공식 : m! / n!(m-n)!
'''
import sys


def factorial(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
    return res


def bridge(n, m):
    return factorial(m) // (factorial(n) * factorial(m - n))


T = sys.stdin.readline()

for tc in range(int(T)):
    N, M = sys.stdin.readline().split()
    print(bridge(int(N), int(M)))