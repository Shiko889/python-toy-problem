def solution(N):
    # Calculate the number of times each letter should occur
    letters_per_letter = N // 15
    remainder = N % 15
    
    # Generate a string of all lowercase letters repeated the calculated number of times
    result = ''.join(chr(ord('a') + i) * letters_per_letter for i in range(15))
    
    # Add remaining characters if any
    result += ''.join(chr(ord('a') + i) for i in range(remainder))
    
    return result

# Test cases
print(solution(3))  # Output: 'abc'
print(solution(5))  # Output: 'abcde'
print(solution(30)) # Output: 'aabbccddeeffgghhiijjkkllmmnnoo'
