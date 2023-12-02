l, r = map(int, input().split())
S = list(input())

ans = S[:l-1] + list(reversed(S[l-1:r])) + S[r:]
print(*ans, sep="")