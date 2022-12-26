import re 
import math

def parse(input):
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip() for line in file_lines]
        input_list.append('')
    
    #splitting input into 2d array, each monkey is a list
    monkey_list = []
    each_monkey = []
    for att in input_list:
        if att == '':
            monkey_list.append(each_monkey)
            each_monkey = []
        else:
            each_monkey.append(att)

    #splitting each monkey's attributes into pertinant data only 
    monkey_data = []
    '''
    monkey_data[0] is integer of the monkey's number
    monkey_data[1] is list of integer starting items 
    monkey_data[2] is list of [0] math symbol and [1] either old value or integer to do math
    monkey_data[3] is integer to test divisibility
    monkey_data[4] is monkey number to give to if test is true
    monkey_data[5] is monkey number to give to if test is false
    '''
    for monkey in monkey_list:
        data = []
        for att in monkey:
            if att == monkey[2]:
                line = att.split()[-2:]
                print(line)
            else:
                line = re.findall('[0-9]+', att)
            line = [int(i) if i.isnumeric() else i for i in line]
            data.append(line)
        monkey_data.append(data)

        
    return monkey_data

def game(monkey_input, rounds):

    monkey_inspections = [0] * len(monkey_input)
    
    for round in range(rounds):
        for monkey_number, turn in enumerate(monkey_input):
            #operation to find worry value
            for item in turn[1]:
                if turn[2][1] == 'old':
                    value = item
                else:
                    value = turn[2][1]
                if turn[2][0] == '+':
                    worry = math.floor((item + value)/3)
                else:
                    worry = math.floor((item * value)/3)
                #check if worry is divisible
                if worry % turn[3][0] == 0:
                    monkey_input[turn[4][0]][1].append(worry)
                else:
                    monkey_input[turn[5][0]][1].append(worry)
                #adding a count to the monkey for an inspection
                monkey_inspections[monkey_number] +=1
            #all items removed so make items empty
            turn[1] = []
    
    top_monkeys = sorted(monkey_inspections,reverse=True)
    print(top_monkeys)
    print(math.prod(top_monkeys[:2])) #product of top 2 monkeys
                    

data = parse('test.txt')
game(data, 20)
