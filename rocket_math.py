import random
import time
import sys

def get_operators(include_add=True,include_sub=True,include_mult=True,include_div=True):
    operators = []
    if include_add == True:
        operators.append("+")
    if include_sub == True:
        operators.append("-")
    if include_mult == True:
        operators.append("*")
    if include_div == True:
        operators.append("/")
    return operators

def calculate_result(digit_1, digit_2, operator):
    if operator == "+":
        return digit_1 + digit_2
    elif operator == "-":
        return digit_1 - digit_2
    elif operator == "*":
        return digit_1 * digit_2
    return digit_1 / digit_2

def print_countdown(operators):
    print(f"Your are practicing with: {operators}")
    time.sleep(2)
    print("Okay! Good Luck. Starting in ... ")
    time.sleep(1)
    print("3 ...")
    time.sleep(1)
    print("2 ...")
    time.sleep(1)
    print("1 ...\nGo!!")
    time.sleep(1)
    
def rocket_math(prob_num):
    '''change the included operators here. 
    I.e. to remove division include the argument include_div = False'''
    operators = get_operators(include_div = False)
    print_countdown(operators)
    start_time = time.time()
    for _ in range(prob_num):
        operator = operators[random.randint(0,len(operators)-1)]
        first_num = random.randint(1,20)
        second_num = random.randint(1,20)
        input_frm_user = input(f"{first_num} {operator} {second_num} =  ")
        result = calculate_result(first_num,second_num, operator)
        while int(input_frm_user) != result:
            print("Nope! Try again:")
            input_frm_user = input(f"{first_num} {operator} {second_num} =  ")
    print(f'Great Job. You took {time.time() - start_time:.4f} seconds to solve {prob_num} problems')

if __name__ == "__main__":
    try:
        rocket_math(int(sys.argv[1]))
    except IndexError as e:
        print(f"Error {e}: Be sure to  include the amount of problems that you would like to practice\nExample: $python3 rocket_math.py 10")