n = int(input())

ac_n = 0
wa_n = 0
tle_n = 0
re_n = 0
for _ in range(n):
    s = input()
    if s == "AC":
        ac_n += 1
    elif s == "WA":
        wa_n += 1
    elif s == "TLE":
        tle_n += 1
    elif s == "RE":
        re_n += 1

print("AC x " + str(ac_n))
print("WA x " + str(wa_n))
print("TLE x " + str(tle_n))
print("RE x " + str(re_n))