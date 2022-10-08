n = int(input())
slogs = list()
slog = 1

while n > 2*slog:
    n -= slog
    slogs.append(slog)
    slog += 1
slogs.append(n)

print(len(slogs))
print(*slogs)