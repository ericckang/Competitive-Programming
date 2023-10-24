

def generate_sequence(n, a, b, c, d):
    sequence = []
    x = d
    for _ in range(n):
        sequence.append(x)
        x = ((a * x + b) % c) + d
    return sequence


def can_be_found(seq, index):
    n = len(seq)
    elem = seq[index]
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2

        if mid == index:
            if (l == mid or max(seq[l:mid]) < elem) and (mid == r or elem < min(seq[mid + 1:r + 1])):
                return True
            else:
                return False

        elif seq[mid] < elem:
            l = mid + 1
        else:
            r = mid - 1

    return False

if __name__ == "__main__":
    n, a, b, c, d = map(int, input().split())
    sequence = generate_sequence(n, a, b, c, d)
    count = sum(can_be_found(sequence, i) for i in range(n))
    print(count)