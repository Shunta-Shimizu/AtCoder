n, k = map(int, input().split())

def sort_large(x):
    x = sorted(list(str(x)), reverse=True)
    a = ""
    for i in x:
        a += str(i)
    
    return int(a)

def sort_small(x):
    x = sorted(list(str(x)))
    a = ""
    for i in x:
        a += str(i)
    
    return int(a)
  
a = n
g1 = sort_large(a)
g2 = sort_small(a)
for i in range(k):
    a = g1 -  g2
    g1 = sort_large(a)
    g2 = sort_small(a)

print(a)