# n, k = map(int, input().split())
# P = list(map(int, input().split()))

# id = []
# for i, p in enumerate(P):
#     id.append([p, i+1])

# id = sorted(id, key=lambda x:x[0])
# # print(id)
# Q = []
# for p, i in id:
#     Q.append(i)

# def max_min(left, right):
#     max_value, min_value = Q[left], Q[left]
#     for i in range(left+1, right):
#         max_value = max(max_value, Q[i])
#         min_value = min(min_value, Q[i])
#     return max_value, min_value

# min_diff = 10**9
# max_value, min_value = Q[0], Q[0]
# left, right = 0, 0

# while right < n:
#     while right < n and right - left < k:
#         right += 1
#         if right < n:
#             max_value = max(max_value, Q[right])
#             min_value = min(min_value, Q[right])
#     if right < n:
#         min_diff = min(min_diff, max_value - min_value)
#         left += 1
#         if left < right:
#             max_value = max(max_value, *Q[left:right])
#             min_value = min(min_value, *Q[left:right])
#         else:
#             max_value, min_value = Q[right], Q[right]
#     else:
#         break

# # print(min_diff)
# print(min_diff)

n, k = map(int, input().split())
P = list(map(int, input().split()))

id = []
for i, p in enumerate(P):
    id.append([p, i+1])

id = sorted(id, key=lambda x:x[0])

Q = []
for p, i in id:
    Q.append(i)

def max_min(left, right):
    max_value, min_value = Q[left], Q[left]
    for i in range(left+1, right):
        max_value = max(max_value, Q[i])
        min_value = min(min_value, Q[i])
    return max_value, min_value

max_value, min_value = max_min(0, k)

min_diff = max_value - min_value

for i in range(1, n-k+1):
    if Q[i-1] == max_value:
        if Q[i+k-1] > max_value:
            max_value = Q[i+k-1]
        elif Q[i+k-1] < min_value:
            min_value = Q[i+k-1]
        else:
            max_value, min_value = max_min(i, i+k)
    elif Q[i-1] == min_value:
        if Q[i+k-1] < min_value:
            min_value = Q[i+k-1]
        elif Q[i+k-1] > max_value:
            max_value = Q[i+k-1]
        else:
            max_value, min_value = max_min(i, i+k)
    
    min_diff = min(min_diff, max_value - min_value)

print(min_diff)
