def most_cals(number_of_top_elves):
   
    with open("day1_input.txt", "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip() for line in file_lines]

    elves = []
    elf_cals = 0

    for item in input_list:
        if item == '':
            elves.append(elf_cals)
            elf_cals = 0
        else:
            elf_cals += int(item)

    elves.sort(reverse=True)

    top_total = sum(elves[:number_of_top_elves])
    return print(top_total)
    
    
most_cals(3)