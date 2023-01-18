from arithmetic_arrange import arithmetic_arranger
from time_calculator import add_time

if __name__ == '__main__':
    # arithmetic arranger
    problems = []
    problem_input = input("Formatting will be number1 + number2, example: 1 + 2\nInput problems to solve:")
    while problem_input != "-1" and len(problems) < 5:
        problems.append(problem_input)
        problem_input = input("Formatting will be number1 + number2, example: 1 + 2\nInput problems to solve:")


    print(arithmetic_arranger(problems, True))
