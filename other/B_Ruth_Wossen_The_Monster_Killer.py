n = int(input())
costs = list(map(int, input().split()))
m = int(input())

# Precompute the prefix sums for both the original costs and the sorted costs
pref_sum = [0] * (n + 1)
pref_sorted = [0] * (n + 1)

sorted_costs = sorted(costs)  # Sort the costs in non-decreasing order

for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + costs[i - 1]
    pref_sorted[i] = pref_sorted[i - 1] + sorted_costs[i - 1]
# Answer Ruth Wossen's questions
for _ in range(m):
    q_type, l, r = map(int, input().split())

    if q_type == 1:
        answer = pref_sum[r] - pref_sum[l - 1]
    else:
        answer = pref_sorted[r] - pref_sorted[l - 1]

    print(answer)
