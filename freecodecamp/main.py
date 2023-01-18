from arithmetic_arrange import arithmetic_arranger
from time_calculator import add_time
import shape_calculator

if __name__ == '__main__':
    # arithmetic arranger
    problems = []
    problem_input = input("Formatting will be number1 + number2, example: 1 + 2\nInput problems to solve:")
    while problem_input != "-1" and len(problems) < 5:
        problems.append(problem_input)
        problem_input = input("Formatting will be number1 + number2, example: 1 + 2\nInput problems to solve:")

    # time calculator
    print(add_time("6:30 PM", "205:12"))
    print()
    print(round(212/60))

    # Polygon Area Calculator
    rect = shape_calculator.Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(2)
    rect.set_width(6)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = shape_calculator.Square(9)
    print(sq.get_area())
    sq.set_side(3)
    print(sq.get_diagonal())
    print(sq.get_picture())

    rect1 = shape_calculator.Rectangle(10, 10)
    rect2 = shape_calculator.Rectangle(4, 8)
    print(rect2.get_amount_inside(rect1))
    