#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes

def main():
    # Read the number of obstacles 'n' and the height of the corridor 'h'.
    n, h = map(int, input().split())

    # Initialize a list to store the cumulative count of obstacles at each level.
    obstacles = [0] * (h + 1)

    for i in range(n):
        # Read the height of the i-th obstacle.
        obstacle = int(input())

        if i % 2 == 0:
            # For even-indexed obstacles start from the bottom.
            obstacles[0] += 1 # Increment the count of obstacles at the bottom level.
            if obstacle < h: # Decrement the count of obstacles at the level corresponding to the height of the obstacle.
                obstacles[obstacle] -= 1
        else:
            # For odd-indexed obstacles start from the top
            obstacles[h - obstacle] += 1 # Increment the count of obstacles at the level corresponding to the top minus the height of the obstacle.

    min_obstacles = n # Initialize min_obstacles to the maximum possible value, which is the total number of obstacles.
    levels = 0 # Initialize the number of levels having min_obstacles.
    current_obstacle = 0 # Initialize the cumulative count of obstacles for the current level.

    for i in range(h):
        # Iterate through each level.
        current_obstacle += obstacles[i] # Update the cumulative count of obstacles for the current level.
        if current_obstacle < min_obstacles:
            # If the current cumulative count is less than the current minimum, update min_obstacles and reset levels to 1.
            min_obstacles = current_obstacle
            levels = 1
        elif current_obstacle == min_obstacles:
            # If the current cumulative count is equal to the current minimum, increment the count of levels having min_obstacles.
            levels += 1

    print(min_obstacles, levels) # Print the minimum number of obstacles and the number of levels having this minimum.


if __name__ == "__main__":
    main()
