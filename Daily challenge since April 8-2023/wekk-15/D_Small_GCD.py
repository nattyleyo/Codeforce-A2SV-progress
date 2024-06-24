from collections import deque

# Input handling
t = int(input())
for _ in range(t):

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    MAX = 10**5  # Assuming MAX is defined somewhere

    freq = [0] * (MAX+1)
    for i in range(N-1):
        freq[arr[i]] += 1

    cnt = [0] * (MAX+1)
    for d in range(1, MAX):
        for v in range(d, MAX+1, d):
            cnt[d] += freq[v]

    dp = [0] * (MAX+1)
    for t in range(N-2, 0, -1):
        K = 0
        val = arr[t]
        primes = []
        while val > 1:
            for p in range(2, int(val**0.5)+1):
                if val % p == 0:
                    primes.append(p)
                    val //= p
                    break
            else:
                primes.append(val)
                break

        q = deque([arr[t]])
        time = t
        ts = [0] * (MAX+1)

        while q:
            val = q.popleft()
            dp[val] += (cnt[val] - 1) * (N - t - 1)
            cnt[val] -= 1

            for p in primes:
                if p > val:
                    continue
                next_val = val // p
                if next_val * p != val:
                    continue
                if ts[next_val] != time:
                    ts[next_val] = time
                    q.append(next_val)
    print(sum(dp))

    # Output dp or whatever you need with dp

