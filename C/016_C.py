string = list(input())

list_str = ["A", "E", "G", "I", "O", "S", "Z"]
list_num = [4, 3, 6, 1, 0, 5, 2]
item_dict = dict(zip(list_str, list_num))
ans = ""
for i in range(len(string)):
    if string[i] in list_str:
        string[i] = item_dict[string[i]]
    ans += str(string[i])
print(ans)
