def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    digit_sums = {}
    max_sum = -1
    for num in A:
        sum_of_digits = digit_sum(num)
        if sum_of_digits in digit_sums:
            max_sum = max(max_sum, num + digit_sums[sum_of_digits])
            digit_sums[sum_of_digits] = max(num, digit_sums[sum_of_digits])
        else:
            digit_sums[sum_of_digits] = num
    return max_sum

# Test cases
# Test case 1
A1 = [51, 71, 17, 42]
print(solution(A1))  # Expected output: 93

# Test case 2
A2 = [42, 33, 60]
print(solution(A2))  # Expected output: 102

# Test case 3
A3 = [51, 32, 43]
print(solution(A3))  # Expected output: -1
