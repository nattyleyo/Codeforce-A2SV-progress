# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the array
    n = int(input())

    # Read the strengths of the participants
    strengths = list(map(int, input().split()))

    # Find the maximum strength except for the current participant
    max_strength_except_current = max(strengths[:])
    strengths.remove(max_strength_except_current)
    max_strength_except_current = max(strengths)

    # Iterate through each participant
    for i in range(n):
        # Calculate the difference between the strength of the participant and the maximum strength except for the current participant
        if strengths[i] == max_strength_except_current:
            print(max_strength_except_current, end=' ')
        else:
            print(max_strength_except_current - strengths[i], end=' ')

    # Print a new line after printing differences for all participants in a test case
    print()
