k, g, m = map(int, input().split())

gnow = 0
mnow = 0
for i in range(k):
    if gnow == g:
        gnow = 0
    elif gnow != g and mnow == 0:
        mnow = m
    else:
        while True:
            if mnow < g:
                gnow += mnow
                mnow = 0
                break
            else:
                diff = g-gnow
                gnow += diff
                mnow -= diff
                break
            
print(gnow, mnow)