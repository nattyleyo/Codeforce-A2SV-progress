t = int(input())

for _ in range(t):
    a = input()
    n = len(a)
    result = list(a)
    parity = [[], []]  # Separate even and odd digits

    for digit in result:
        if int(digit) % 2 == 0:
            parity[0].append(digit)
        else:
            parity[1].append(digit)

    i = 0  # Index for even digits
    j = 0  # Index for odd digits

    while i < len(parity[0]) and j < len(parity[1]):
        if parity[0][i] < parity[1][j]:
            result[i + j] = parity[0][i]
            i += 1
        else:
            result[i + j] = parity[1][j]
            j += 1

    # Append remaining digits, if any
    while i < len(parity[0]):
        result[i + j] = parity[0][i]
        i += 1

    while j < len(parity[1]):
        result[i + j] = parity[1][j]
        j += 1

    print("".join(result))
