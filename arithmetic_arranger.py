import sys


def arithmetic_arranger(lst, countUp):
    number_ones = []
    number_twos = []
    operators = []
    totalsum = []
    index = 0
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    if len(lst) > 5:
        print("Error: Too many problems.")
        sys.exit()
    for i in lst:
        splited_list = i.split()
        num1 = str(splited_list[0])
        num2 = str(splited_list[2])
        operator = splited_list[1]
        if operator == "-":
            totalsum.append(int(num1) - int(num2))
        elif operator == "+":
            totalsum.append(int(num1) + int(num2))
        else:
            print("Error: Operator must be '+' or '-'.")
            sys.exit()
        if len(splited_list) != 3:
            print("Error: Too much numbers")
            sys.exit()
        if not num1.isnumeric() or not num2.isnumeric():
            print("Error: Numbers must only contain digits.")
            sys.exit()
        if len(num1) > 4:
            print("Error: Numbers cannot be more than four digits.")
            sys.exit()
        elif len(num2) > 4:
            print("Error: Numbers cannot be more than four digits.")
            sys.exit()
        operators.append(operator)
        number_ones.append(num1)
        number_twos.append(num2)
    for x in range(len(lst)):
        bigger_number = (max(int(number_ones[index]), int(number_twos[index])))
        smaller_number = (min(int(number_ones[index]), int(number_twos[index])))
        smaller_number = str(smaller_number)
        bigger_number = str(bigger_number)
        xx = (str(number_ones[index]).rjust(int(len(bigger_number)) + 2))
        line1 = line1 + (str(number_ones[index]).rjust(int(len(bigger_number)) + 2)) + "    "
        line2 = line2 + (operators[index] + number_twos[index].rjust(int(len(bigger_number) + 1))) + "    "
        line3 = line3 + ("-" * len(xx)) + "    "
        line4 = line4 + (str(totalsum[index]).rjust(len(xx))) + "    "
        index = index + 1
    print(line1)
    print(line2)
    print(line3)
    if countUp == True:
        print(line4)
