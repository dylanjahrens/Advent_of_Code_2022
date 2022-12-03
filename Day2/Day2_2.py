def strategy_guide():
   
    with open("Day2_input.txt", "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip().split(' ') for line in file_lines]

    total_score = 0

    for round in input_list:
        if round[1] == 'X': #lose
            if round[0] == 'A':
                total_score += 3
            elif round[0] == 'B':
                total_score += 1
            elif round[0] == 'C':
                total_score += 2
        elif round[1] == 'Y': #tie
            total_score +=3
            if round[0] == 'A':
                total_score += 1
            elif round[0] == 'B':
                total_score += 2
            elif round[0] == 'C':
                total_score += 3
        elif round[1] == 'Z': #win
            total_score +=6
            if round[0] == 'A':
                total_score += 2
            elif round[0] == 'B':
                total_score += 3
            elif round[0] == 'C':
                total_score += 1
    
    print(total_score)


strategy_guide()