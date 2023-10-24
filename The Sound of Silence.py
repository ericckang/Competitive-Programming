def main():
    from collections import deque

    def detect_silence(n, m, t, samples):
        # List to store the starting positions of detected silences
        silence_starts = []

        # max_deque and min_deque are deques that will keep track of the maximum
        # and minimum values within the current window of m samples respectively.
        max_deque, min_deque = deque(), deque()

        # Process the first m samples to initialize the deques
        for i in range(m):
            # Remove samples from the back while they are smaller/equal than the current sample
            while max_deque and samples[i] >= samples[max_deque[-1]]:
                max_deque.pop()
            while min_deque and samples[i] <= samples[min_deque[-1]]:
                min_deque.pop()

            # Add the current sample's index to the deques
            max_deque.append(i)
            min_deque.append(i)

        # Check for silence in the initial window
        if samples[max_deque[0]] - samples[min_deque[0]] <= t:
            silence_starts.append(1)

        # Slide the window across the rest of the samples
        for i in range(m, n):
            # Same process as before to maintain the deques for the current window
            while max_deque and samples[i] >= samples[max_deque[-1]]:
                max_deque.pop()
            while min_deque and samples[i] <= samples[min_deque[-1]]:
                min_deque.pop()

            max_deque.append(i)
            min_deque.append(i)

            # Remove indices that are out of the current window from the front of the deques
            while max_deque and max_deque[0] <= i - m:
                max_deque.popleft()
            while min_deque and min_deque[0] <= i - m:
                min_deque.popleft()

            # Check for silence in the current window
            if samples[max_deque[0]] - samples[min_deque[0]] <= t:
                silence_starts.append(i - m + 2)

        return silence_starts

    # Read input data: length of samples, window size, and threshold for silence detection
    n, m, t = map(int, input().split())
    samples = list(map(int, input().split()))

    # Find all silences in the samples
    silences = detect_silence(n, m, t, samples)

    # Output the result
    if not silences:
        print("NONE")
    else:
        for start in silences:
            print(start)

if __name__ == "__main__":
    main()
