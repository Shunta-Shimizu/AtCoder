import math
def solve(N, M, K):
    if N > M:
        N, M = M, N

    lcm_value = (N * M) // math.gcd(N, M)

    lower_bound = N
    upper_bound = max(N, M) * K

    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2

        count = mid // N + mid // M - (mid // lcm_value)*2

        if count < K:
            lower_bound = mid + 1
        else:
            upper_bound = mid

    return lower_bound

n, m, k = map(int, input().split())
print(solve(n, m, k))