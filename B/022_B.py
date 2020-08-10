RIKKOHO_NUM, YUKENSYA_NUM, K = map(int, input().split())
vote_list = []
for i in range(K):
    vote_list.append(int(input()))

key_list = list(range(1, RIKKOHO_NUM+1))
val_list = list([0]*RIKKOHO_NUM)
sijisya = dict(zip(key_list, val_list))
undetermined = YUKENSYA_NUM

for i in vote_list:
    if(undetermined > 0):
        sijisya[i] += 1
        undetermined -= 1
    for j in key_list:
        if j != i:
            if sijisya[j] > 0:
                sijisya[j] -= 1
                sijisya[i] += 1

ans_list = [i+1 for i,
            v in enumerate(sijisya.values()) if v == max(sijisya.values())]
for i in ans_list:
    print(i)
