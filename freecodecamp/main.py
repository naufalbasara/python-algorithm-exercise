from arithmetic_arrange import arithmetic_arranger
from .time-calculator.time_calculator import add_time
import shape_calculator
# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

if __name__ == '__main__':
    # arithmetic arranger
    problems = []
    problem_input = input("Formatting will be number1 + number2, example: 1 + 2\nInput problems to solve:")
    while problem_input != "-1" and len(problems) < 5:
        problems.append(problem_input)
        problem_input = input("Formatting will be number1 + number2, example: 1 + 2\nInput problems to solve:")

    print(arithmetic_arranger(problems,True))


    # Time Calculator
    import prob_calculator

    # Probability Calculator
    prob_calculator.random.seed(95)
    hat = prob_calculator.Hat(blue=4, red=2, green=6)
    probability = prob_calculator.experiment(
        hat=hat,
        expected_balls={"blue": 2,
                        "red": 1},
        num_balls_drawn=4,
        num_experiments=3000)
    print("Probability:", probability)

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


    #Budget App
    food = budget.Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = budget.Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = budget.Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)
    print(auto)
    print(create_spend_chart([food, clothing, auto]))

    food = budget.Category("Food")
    entertainment = budget.Category("Entertainment")
    business = budget.Category("Business")

    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    print(food)
    print(entertainment)
    print(business)
    print(create_spend_chart([business, food, entertainment]))
    # Run unit tests automatically
    main(module='test_module', exit=False)
    