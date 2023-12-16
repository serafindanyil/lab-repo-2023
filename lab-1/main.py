print("Select part:\n part_1 (1)\n part_2.1(2)\n part_2.2(3)")
select_part = int(input("enter: "))

if select_part == 1:
    exec(open('part_1.py').read())
elif select_part == 2:
    exec(open('part_2_1.py').read())
elif select_part == 3:
    exec(open('part_2_2.py').read())