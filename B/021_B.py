N = int(input())
string_list = []
ans_list = []


def convert(string_list):
    # print(string_list[-1], string_list[-2])
    if string_list[-1] == "s" or string_list[-1] == "o" or string_list[-1] == "x" or (string_list[-1] == "h" and (string_list[-2] == "s" or string_list[-2] == "c")):
        string_list.append("es")
    elif string_list[-1] == 'f':
        string_list.pop(-1)
        string_list.append("ves")
    elif string_list[-1] == 'e' and string_list[-2] == "f":
        string_list.pop(-1)
        string_list.pop(-1)
        string_list.append("ves")
    elif string_list[-1] == "y" and string_list[-2] not in ["a", "i", "u", "e", "o"]:
        string_list.pop(-1)
        string_list.append("ies")
    else:
        string_list.append("s")
    ans = "".join(string_list)
    return ans


for i in range(N):
    string = list(input())
    strings = convert(string)
    ans_list.append(strings)

for i in ans_list:
    print(i)
