N = int(input())
num_16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

a = N // 16
b = N % 16

num = num_16[a] + num_16[b]

print(num)