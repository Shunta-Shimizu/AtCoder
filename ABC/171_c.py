import string
n = int(input())

ans = ""
alphabet = list(string.ascii_lowercase)

while n > 0:
    n -= 1
    ans += alphabet[n%26]

    n //= 26

print("".join(list(reversed(ans))))