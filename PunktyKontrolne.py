n = int(input())
tab = []
for i in range(n):
    tab.append(tuple(map(float, input().split())))
x, y = map(float, input().split())
for i in range(n):
    tab[i] = ( ((tab[i][0] - x)**2 + (tab[i][1] - y)**2)**0.5, tab[i] )
tab.sort()
print(tab)
