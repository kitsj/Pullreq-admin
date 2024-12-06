import sys
N = int(sys.stdin.readline())
word = []
for i in range(N):
    word.append(input())
arr = list(set(word))
arr = sorted(arr)
for i in range(len(arr)):
    print(arr[i])
    