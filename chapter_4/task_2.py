n, v = map(int, input().split())

# read data and sort by relative cost
items = sorted([list(map(int, input().split())) for _ in range(n)],
               key=lambda item: item[0]/item[1], reverse=True)

cost = 0
for item in items:
    if v >= item[1]:
        v -= item[1]
        cost += item[0]
    else:
        k = v / item[1]
        cost += item[0] * (v / item[1])
        break

print(cost)

