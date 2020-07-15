for _ in range(int(input())):
    n = int(input())
    i = 1
    count = 0
    while True:
        if pow(5, i) > n:
            break
        count += n // pow(5, i)
        i += 1
    print(count)
