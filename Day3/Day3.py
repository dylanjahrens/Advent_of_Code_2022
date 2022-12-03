def rucksacks(input):
   
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip() for line in file_lines]

    rucksacks = []
    for line in input_list:
        halfway = len(line)//2
        rucksack = []
        rucksack.append(line[:halfway])
        rucksack.append(line[halfway:])
        rucksacks.append(rucksack)
    
    dup_items = []
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                dup_items.append(item)
                break

    priority_sum = 0
    for item in dup_items:
        if item.isupper():
            value = ord(item) - 38
        else:
            value = ord(item) - 96
        priority_sum += value

    return print(priority_sum)


rucksacks('Day3_input.txt')