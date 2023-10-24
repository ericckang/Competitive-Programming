def main():
    def interesting_subsequences_count(n, seq):
        pi_sum = 2 + 7 + 1 + 8 + 2 + 8 + 1 + 8 + 2 + 8  # Sum of the first ten digits of Euler’s constant
        prefix_sum_freq = {0: 1}  # Prefix sum frequency with sum 0 occurring once.
        count, prefix_sum = 0, 0

        for num in seq:
            prefix_sum += num
            count += prefix_sum_freq.get(prefix_sum - pi_sum, 0)
            prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1

        return count

    # Read the input and solve
    t = int(input().strip())  # Number of test cases

    for i in range(t):
        if i != 0:  # If it's not the first test case, discard the blank line
            input()
        n = int(input().strip())  # Read the length of sequence for current test case
        seq = list(map(int, input().split()))
        print(interesting_subsequences_count(n, seq))

if __name__ == "__main__":
    main()