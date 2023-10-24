def main():
    def count_possible_pivots(n, arr):
        # initialize leftMax and rightMin arrays with zeros and infinity
        leftMax = [0] * n
        rightMin = [float('inf')] * n

        # fill in the leftMax array
        leftMax[0] = arr[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], arr[i])

        # fill in the rightMin array
        rightMin[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            rightMin[i] = min(rightMin[i + 1], arr[i])

        # count how many integers could have been the chosen pivot
        count = 0
        for i in range(n):
            # the conditions for a number to be the pivot
            if (i == 0 or arr[i] > leftMax[i - 1]) and (i == n - 1 or arr[i] < rightMin[i + 1]):
                count += 1

        return count

    # read input
    n = int(input())
    arr = list(map(int, input().split()))

    # output the result
    print(count_possible_pivots(n, arr))

if __name__ == "__main__":
    main()