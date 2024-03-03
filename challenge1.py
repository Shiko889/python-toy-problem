def solution(A):
    # Calculate the length of A
    length = len(A)

    # Establish the sum of all the bricks in A
    total = sum(A)

    # Initialize count to track moves
    count = 0

    # Check if it is possible to redistribute 10 bricks to each box
    if total / length != 10:
        return -1

    # Iterate through the indices of the boxes in A
    for i in range(length - 1): 

        # Check that box at index i has more than 10 bricks
        # Check that the box after it is less than 10
        # Subtract 1 brick from the initial box and add it to the next box
        # Track number of the moves that happen for that
        while A[i] > 10 and A[i + 1] < 10:
            A[i] -= 1
            A[i + 1] += 1
            count += 1

        # Check that box at index i has more than 10 bricks
        # Check that the box before it has less than 10 bricks
        # Subtract 1 brick from the initial box and add it to the box before it
        # Track number of the moves that happen for that
        while A[i] > 10 and A[i - 1] < 10:
            A[i] -= 1
            A[i - 1] += 1
            count += 1

        # Check that box at index i has more bricks than the one after it 
        # Check that the box after it has less than 10 bricks
        # Subtract 1 brick from the initial box and add it to the next box
        # Track number of the moves that happen for that
        while A[i] > A[i + 1] and A[i + 1] < 10:
            A[i] -= 1
            A[i + 1] += 1
            count += 1

        # Check that box at index i has more bricks than the one after it 
        # Check that the box before it has less than 10 bricks
        # Subtract 1 brick from the initial box and add it to the box before it
        # Track number of the moves that happen for that
        while A[i] > A[i - 1] and A[i - 1] < 10:
            A[i] -= 1
            A[i - 1] += 1
            count += 1

    return count

# Test cases
print(solution([19, 2])) # Expected output: -1
print(solution([19, 1])) # Expected output: 9
print(solution([21, 2, 7])) # Expected output: 11
