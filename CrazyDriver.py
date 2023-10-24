def min_cost(gates, tolls, opening_times, start_gate, start_time, end_gate):
    dp = [[float('inf')] * 2001 for _ in range(gates)]
    dp[start_gate][start_time] = 0

    for time in range(start_time, opening_times[end_gate] + gates):
        for gate in range(gates):
            # Stay at the current gate
            if time + 1 < 2001:
                dp[gate][time + 1] = min(dp[gate][time + 1], dp[gate][time])

            # Move to the left gate
            if gate > 0:
                dp[gate - 1][time + 1] = min(dp[gate - 1][time + 1], dp[gate][time] + tolls[gate - 1])

            # Move to the right gate
            if gate < gates - 1:
                dp[gate + 1][time + 1] = min(dp[gate + 1][time + 1], dp[gate][time] + tolls[gate])

    return dp[end_gate][opening_times[end_gate]]


# Parse the inputs
gates = int(input())
tolls = list(map(int, input().split()))
opening_times = list(map(int, input().split()))

# Here start_gate is 0 and start_time is 0
# as mentioned in the prompt, and end_gate is gates - 1
print(min_cost(gates, tolls, opening_times, 0, 0, gates - 1))
