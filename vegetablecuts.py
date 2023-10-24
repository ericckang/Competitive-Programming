from queue import Queue


def min_cuts(r, n, weights):
    # Step 1: Initialize the BFS
    q = Queue()
    q.put((weights, 0))  # Each state is represented as (weights, cuts))
    visited = set()  # To store the visited states and avoid repetition
    visited.add(tuple(sorted(weights)))

    while not q.empty():
        curr_weights, cuts = q.get()
        min_w = min(curr_weights)
        max_w = max(curr_weights)

        # Step 2: Check if the current state satisfies the condition
        if min_w / max_w >= r:
            return cuts

        # Step 3: Generate all possible next states by cutting the largest vegetable
        for i in range(n):
            if curr_weights[i] == max_w:
                # Find a cut that is closest to the minimum weight without exceeding it
                next_weights = list(curr_weights)
                next_piece = max(min_w, max_w - min_w)
                next_weights[i] = max_w - next_piece

                # Add the new piece created from the cut
                next_weights.append(next_piece)
                sorted_weights = tuple(sorted(next_weights))

                # Add the new state to the queue if it has not been visited before
                if sorted_weights not in visited:
                    q.put((sorted_weights, cuts + 1))
                    visited.add(sorted_weights)

    return -1  # Should not reach here, just a safety net


# Sample Input 1
r = 0.99
n = 3
weights = [2000, 3000, 4000]
print(min_cuts(r, n, weights))  # Output: 6

# Sample Input 2
r = 0.80
n = 2
weights = [1000, 1400]
print(min_cuts(r, n, weights))  # Output: 3
