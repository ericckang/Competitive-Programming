def main ():
    import math

    # Read n and m
    n, m = map(int, input().split())

    # Read the known angles in a single line
    known_angles = list(map(int, input().split()))

    num = 360
    for t in known_angles:
        num = math.gcd(num, t)

    # Read the angles to test
    test_angles = list(map(int, input().split()))

    for t in test_angles:
        if t % num == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()