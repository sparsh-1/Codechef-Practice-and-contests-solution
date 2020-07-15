for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    diff = 10000000000
    for i in range(n - 1):
        if arr[i + 1] - arr[i] < diff:
            diff = arr[i + 1] - arr[i]
    print(diff)
