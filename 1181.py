import sys
N = int(sys.stdin.readline())
word = []
for n in range(N):
    word.append(input())
arr = list(set(word))
arr = sorted(arr)
for n in range(len(arr)):
    print(arr[n])
    
