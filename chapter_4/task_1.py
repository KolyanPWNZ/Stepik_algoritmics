list_line = sorted([list(map(int, input().split())) for i in range(int(input()))],
                   key= lambda data: data[1])
points_list = [list_line[0][1]]
for l, r in list_line:
    if l > points_list[-1]:
        points_list.append(r)

print(len(points_list))
print(*points_list)








