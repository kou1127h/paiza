import itertools

N = int(input())

mahoujin = []


def colSum(c, N, array):
    ans = 0
    for i in range(N):
        ans += array[i][c]
    return ans


def exSum(N, array):
    ans1 = 0
    ans2 = 0
    for i in range(N):
        ans1 += array[i][N - 1 - i]
    for i in range(N):
        ans2 += array[i][i]
    return [ans1, ans2]


def appendSum(sums, mahoujin, N):
    for i in range(N):
        sums.append(sum(mahoujin[i]))

    for i in range(N):
        sums.append(colSum(i, N, mahoujin))

    sums.append(exSum(N, mahoujin)[0])
    sums.append(exSum(N, mahoujin)[1])
    return sums


def printMahoujin(mahoujin):
    for i in range(len(mahoujin)):
        print(*mahoujin[i])


for i in range(N):
    row = map(int, input().split())
    mahoujin.append(list(row))

sums = []
appendSum(sums, mahoujin, N)

sums = list(set(sums))
sorted_items = sorted(sums, reverse=True)

ans_sml = sorted_items[0] - sorted_items[1]
ans_big = sorted_items[0] - sorted_items[2]

zero_position = []
for i in range(N):
    for j in range(N):
        if mahoujin[i][j] == 0:
            zero_position.append([i, j])

mahoujin[zero_position[0][0]][zero_position[0][1]] = ans_sml
mahoujin[zero_position[1][0]][zero_position[1][1]] = ans_big

try_sums = []
appendSum(try_sums, mahoujin, N)
sorted_try_sums = sorted(try_sums)
if sorted_try_sums[-1] - sorted_try_sums[0] == 0:
    printMahoujin(mahoujin)
else:
    mahoujin[zero_position[0][0]][zero_position[0][1]] = ans_big
    mahoujin[zero_position[1][0]][zero_position[1][1]] = ans_sml
    printMahoujin(mahoujin)
