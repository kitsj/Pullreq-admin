import sys
while True:
    w = sys.stdin.readline().strip()
    if w == "0":
        break
    wl1 = list(w)
    wl2 = list(w)
    wl2.reverse()
    if wl1 == wl2:
        print("yes")
    else:
        print("no")