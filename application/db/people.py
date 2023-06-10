import random as r


data_for_choice = ('нам не известны', 'ушли в самоволку', 'обедают', 'смотрят котиков на YouTube',
                   '- обладатели премии самый быстрый alt+tab на диком западе', 'передают Вам привет')


def get_employees(department):
    return f'Сотрудники отдела {department} {r.choice(data_for_choice)}'
