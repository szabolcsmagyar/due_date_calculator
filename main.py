from src.calculator.due_date_calculator import dueDateCalculator


def main():
    result = dueDateCalculator("2021-07-06 12:00", 3).run()
    print(result)


if __name__ == "__main__":
    main()
