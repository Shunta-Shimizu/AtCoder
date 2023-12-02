n = int(input())
length_list = list(map(int, input().split()))

print(length_list.index(max(length_list)) + 1)