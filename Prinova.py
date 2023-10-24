def main():
    n = int(input())
    boys = sorted(list(map(int, input().split())))
    a, b = map(int, input().split())

    max_gap = 0
    name = a

    # Consider the gap from the start of the range to the first boy's name
    gap_from_start = boys[0] - a
    if gap_from_start > max_gap:
        max_gap = gap_from_start
        name = a + 1 if a % 2 == 0 else a

    # Consider the gap from the last boy's name to the end of the range
    gap_from_end = b - boys[-1]
    if gap_from_end > max_gap and boys[-1] <= b:
        max_gap = gap_from_end
        name = b - 1 if b % 2 == 0 else b

    # Find the largest gap between the boys within the given range
    for i in range(1, n):
        if boys[i] <= b and boys[i - 1] >= a:
            gap = (boys[i] - boys[i - 1]) // 2
            if gap > max_gap:
                max_gap = gap
                # set name to the odd number at the midpoint of the largest distance
                name = boys[i - 1] + gap
                if name % 2 == 0:
                    name -= 1

    print(name)

if __name__ == "__main__":
    main()