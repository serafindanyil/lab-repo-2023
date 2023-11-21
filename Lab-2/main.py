i = 0
while i < 2:
    print("Choose script" '\n', "1.Part 1" '\n', "2.Part 2")
    __part_script = int(input("Enter the part: "))
    print('\n' * 3)
    if __part_script == 1:
        import part1
        i += 1
    else:
        import part2
        i += 1
    print('\n' * 3)
