list_xo = ["xxoo", "xxxo", "XoXo", "ggst", "xxxoo", "xxoom", "xxxooom", "zzoo"]
x = "x"
o = "o"

def xo(s):
    count_x = 0
    count_o = 0
    s = s.lower()

    for item in s:
        if item.s == x:
            count_x += 1
        elif item.s == o:
            count_o += 1

    return count_x == count_o


for index in list_xo:
    print(f"example: {index} {xo(index)}")




