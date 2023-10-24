# Author: Eric Kang
# It is not ok to share my code anonymously for educational purposes
def calculate_min_loss(rooms_to_close, current_row, closed_status, gallery, memoization):
    # Constants representing the closed status of rooms for readability and error prevention.
    NONE_CLOSED, RIGHT_CLOSED, LEFT_CLOSED = 0, 1, 2

    # Base cases for the recursive function.
    if rooms_to_close == 0:
        return 0  # No more rooms need to be closed.
    if current_row == -1:
        return 105 * 205  # Represents a large cost when we run out of rooms.

    # Retrieving already calculated results for efficiency.
    if memoization[rooms_to_close][current_row][closed_status] > -1:
        return memoization[rooms_to_close][current_row][closed_status]

    # Recursive case handling by considering different room closure scenarios.
    result = calculate_min_loss(rooms_to_close, current_row - 1, NONE_CLOSED, gallery, memoization)

    # Adjusting the result based on the status of adjacent rooms to avoid invalid room closures.
    if closed_status != NONE_CLOSED:
        adjustment_value = gallery[current_row][1] if closed_status == RIGHT_CLOSED else gallery[current_row][0]
        result = min(result, calculate_min_loss(rooms_to_close - 1, current_row - 1, closed_status, gallery,
                                                memoization) + adjustment_value)
    else:
        # Considering both options when no adjacent room is closed.
        close_right = calculate_min_loss(rooms_to_close - 1, current_row - 1, RIGHT_CLOSED, gallery, memoization) + \
                      gallery[current_row][1]
        close_left = calculate_min_loss(rooms_to_close - 1, current_row - 1, LEFT_CLOSED, gallery, memoization) + \
                     gallery[current_row][0]
        result = min(result, min(close_right, close_left))

    # Saving the result to avoid re-computation in future calls.
    memoization[rooms_to_close][current_row][closed_status] = result
    return result


def main():
    # Processing multiple test cases until a terminating signal is received.
    while True:
        num_rows, rooms_to_close = map(int, input().strip().split())

        # Check for the end of the input indicator.
        if num_rows + rooms_to_close == 0:
            break

        # reading input values.
        total_value, gallery_values = 0, []
        for _ in range(num_rows):
            row_values = list(map(int, input().strip().split()))
            total_value += sum(row_values)
            gallery_values.append(row_values)

        # Preparing memoization table to store intermediate results.
        memoization = [[[-1 for _ in range(3)] for _ in range(num_rows)] for _ in range(rooms_to_close + 1)]

        # Compute the optimal value after closures and display it.
        retained_value = total_value - calculate_min_loss(rooms_to_close, num_rows - 1, NONE_CLOSED, gallery_values,
                                                          memoization)
        print(retained_value)

if __name__ == "__main__":
    main()
