#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes

import math

def calculate_catenary_length(a, distance):
    # Calculate the length of the catenary using the formula a * cosh(distance / (2 * a)) - a. where 'a' is a parameter of the catenary, and 'distance' is the distance between the anchor points.
    return a * math.cosh(distance / (2 * a)) - a


def find_a(distance, length, tolerance = 1e-5):
    # Initialize the bounds for the binary search to find the 'a' parameter value.
    lower_bound = 0
    upper_bound = distance ** 2

    # Perform a binary search to find the 'a' parameter value within the specified tolerance.
    while True:
        mid = (lower_bound + upper_bound) / 2
        calculated_length = calculate_catenary_length(mid, distance)

        # If the calculated length is within the tolerance of the desired length, return the current 'a' value.
        if abs(length - calculated_length) < tolerance:
            return mid

        # Adjust the bounds based on the comparison between the calculated length and the desired length.
        if length < calculated_length:
            lower_bound = mid
        else:
            upper_bound = mid


def main():
    # Take input values for distance between anchor points and desired sag (length).
    distance, length = map(int, input().split())

    # Calculate the 'a' parameter of the catenary using the find_a function.
    a = find_a(distance, length)

    # Calculate and print the length of the cable needed using the formula 2 * a * sinh(distance / (2 * a))
    print(2 * a * math.sinh(distance / (2 * a)))


if __name__ == "__main__":
    main()
