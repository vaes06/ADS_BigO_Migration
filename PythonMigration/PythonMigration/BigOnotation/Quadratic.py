
def CreateAllPairs(n):
    x = 1
    while x <= n:
        y = 1
        while y <= n:
            print(x, y)
            y = y + 1
        x = x + 1

n = 5
CreateAllPairs(n)