from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime as dt


def main():
    print(f'Дата: {dt.now().strftime("%d-%m-%Y")}')
    print(calculate_salary(65000, 1.3))
    print(get_employees('айти'))


if __name__ == '__main__':
    main()
