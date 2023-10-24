#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes

def main():
    # Get the number of papers the researcher has written
    n = int(input())

    # Create a list of the number of citations for each paper
    citations = [int(input()) for _ in range(n)]

    # Sort the list of citations in descending order for easier calculation of h-Index
    citations.sort(reverse=True)

    # Initialize h_index variable to 0. This will store the highest h-Index value.
    h_index = 0

    # Iterate through the list of sorted citations to calculate h-Index
    for i in range(n):
        # If the number of citations for the ith paper is greater than or equal to i + 1,
        # Update the h_index to i + 1.
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            # If the number of citations for the ith paper is less than i + 1,
            # We can break out of the loop as further checking is not required.
            break

    # Output the calculated h_Index
    print(h_index)

if __name__ == "__main__":
    main()
