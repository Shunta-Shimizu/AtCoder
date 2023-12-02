class Pizza:
    def solve(self, a, b, c, x, y):
        if a+b < 2*c:
            ans = a*x + b*y
        elif a+b >= 2*c:
            if a >= 2*c and b >= 2*c:
                ans = c*max(x, y)*2
            elif a >= 2*c and b < 2*c:
                if min(x, y) == x:
                    ans = c*min(x, y)*2 + b*(y-x)
                else:
                    ans = c*max(x, y)*2
            elif a < 2*c and b >= 2*c:
                if min(x, y) == y:
                    ans = c*min(x, y)*2 + a*(x-y)
                else:
                    ans = c*max(x, y)*2
            else:
                if min(x, y) == x:
                    ans = c*min(x, y)*2 + b*(y-x)
                else:
                    ans = c*min(x, y)*2 + a*(x-y)

        return ans

a, b, c, x, y = map(int, input().split())
print(Pizza().solve(a, b, c, x, y))


