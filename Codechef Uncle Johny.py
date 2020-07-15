for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    val = arr[k - 1]
    print(sorted(arr).index(val) + 1)
