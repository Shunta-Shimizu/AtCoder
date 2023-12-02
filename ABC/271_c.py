N = int(input())
# A = list(map(int, input().split()))

# read_count = 1
# A_read = A
# for i in A:
#     if (read_count not in A_read) and (read_count-1 <= len(A_read) - 2):
#         del A_read[-2:]
#         A_read.insert(read_count-1, read_count)
#     read_count += 1

# len_A_read = len(A_read)
# if len_A_read == 1 and A_read[-1] != 1:
#     print(0)
# elif len_A_read == 1 and A_read[-1] == 1:
#     print(1)
# elif A_read[-1] != len_A_read:
#     print(A_read[-2])
# else:
#     print(A_read[-1])

A = set(map(int, input().split()))

book_num = 0
while N >= 0:
    if book_num + 1 in A:
        N -= 1
    else:
        N -= 2
    book_num += 1

print(book_num-1)
