import sys

print("minbeom")
print("minbeom")
T = int(sys.stdin.readline().strip())
n = list(map(int,sys.stdin.readline().split()))
n.sort()
print(n[0]*n[-1])
