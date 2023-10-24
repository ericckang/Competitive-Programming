def main():
    INF = 10000

    test = int(input().strip())

    for _ in range(test):
        payable = int(input().strip())
        N = int(input().strip())
        A = [int(input().strip()) for _ in range(N)]
        M = [INF] * (10001)
        M[0] = 0

        for coin in A:
            for j in range(10000, 0, -1):
                if j - coin >= 0 and M[j - coin] + 1 < M[j]:
                    M[j] = M[j - coin] + 1

        i = payable
        while M[i] == INF:
            i += 1

        print(i, M[i])


if __name__ == "__main__":
    main()