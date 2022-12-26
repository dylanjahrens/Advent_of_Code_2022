import re 
import math

def get_monkey_data(input):

    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip() for line in file_lines]
        input_list.append('')

    monkey_list = []
    each_monkey = []
    for att in input_list:
        if att == '':
            monkey_list.append(each_monkey)
            each_monkey = []
        else:
            each_monkey.append(att)

    monkeys = dict()
    for monkey in monkey_list:
        id = int(re.findall("(\d+)", monkey[0])[0])
        monkeys[id] = dict()
        monkeys[id]["items"] = [int(i) for i in re.findall("(\d+)", monkey[1])]
        #operation, operand = re.findall("(\+|\*)\s(old|\d+)", monkey[2])[0]
        operation, operand = monkey[2].split()[-2:]
        monkeys[id]["opn"] = operation
        monkeys[id]["op"] = operand
        monkeys[id]["div_by"] = int(re.findall("(\d+)", monkey[3])[0])
        monkeys[id]["true_id"] = int(re.findall("(\d+)", monkey[4])[0])
        monkeys[id]["false_id"] = int(re.findall("(\d+)", monkey[5])[0])
        monkeys[id]["inspected"] = 0

    return monkeys

def game(monkeys, task, rounds):

    mod_all = 1
    for div_by in [m["div_by"] for m in monkeys.values()]:
        mod_all *= div_by

    for r in range(1,rounds+1):
        for id, m in monkeys.items():
            while monkeys[id]["items"]:
                worry = monkeys[id]["items"].pop(0)
                monkeys[id]["inspected"] += 1
                op = worry if m["op"] == "old" else int(m["op"])
                if m["opn"] == '*':
                    worry *= op
                else:
                    worry += op
                if task == 1: #part1 
                    worry = math.floor((worry / 3))
                else: #part 2
                    worry = worry % mod_all
                if worry % m["div_by"] == 0:
                    monkeys[m["true_id"]]["items"].append(worry)
                else:
                    monkeys[m["false_id"]]["items"].append(worry)
    
    inspections = [m['inspected'] for m in monkeys.values()]
    #print(inspections)
    sorted_inspections = sorted(inspections,reverse=True)
    print(math.prod(sorted_inspections[:2]))
                

monkeys1 = get_monkey_data('Day11_input.txt')
game(monkeys1, 1, 20)

monkeys2 = get_monkey_data('Day11_input.txt')
game(monkeys2, 2, 10000)

