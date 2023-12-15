list_xo = ["xxoo", "xxxo", "XoXo", "ggst", "xxxoo", "xxoom", "xxxooom", "zzoo"]
x = "x"
o = "o"

def xo_function(index):
    count_x = 0
    count_o = 0

    for item in index:
        if item.lower() == x:
            count_x += 1
        elif item.lower() == o:
            count_o += 1

    return count_x == count_o

for index in list_xo:
    print(f"example: {index} {xo_function(index)}")
