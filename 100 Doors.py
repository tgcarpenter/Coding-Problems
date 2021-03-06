def get_final_opened_doors(num_doors):
    door = False
    doors = [door for n in range(num_doors)]

    count = 1
    while count <= num_doors:
        count2 = count
        while count2 <= num_doors:
            if doors[count2 - 1]:
                doors[count2 - 1] = False
            else:
                doors[count2 - 1] = True
            count2 += count
        count += 1

    open_doors = [(x[0] + 1) for x in enumerate(doors) if x[1] is True]
    return open_doors


print(get_final_opened_doors(100))
