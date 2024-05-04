def specific_action_two_numbers(action: int, number_1: int, number_2: int) -> int:
    # sum = number_1 + number_2
    # number_1 = max(number_1, number_2)
    # number_2 = sum - number_1
    number_1, number_2 = max(number_1, number_2), min(number_1, number_2)
    if action == 1:
        return number_1 + number_2
    elif action == 2:
        return number_1 - number_2
    elif action == 3:
        return number_1 * number_2
    elif action == 4 and number_2 != 0 and number_1 % number_2 == 0:
        return number_1 // number_2
    else:
        return -1

def specific_action_one_number(action: int, number: int) -> int:
    if action == 0:
        return number
    elif action == 1:
        return number * 2
    elif action == 2:
        return number * 3
    elif action == 3 and number % 2 == 0:
        return number // 2
    elif action == 4 and number % 3 == 0:
        return number // 3
    else:
        return -1

def correct_answer(action_two_numbers: int, actions_one_number: list, answer_and_numbers: list, order: list) -> bool:
    mistakes = []
    answer_about_mistake = ['сотен', 'десятков', 'единиц']
    for i in range(3):
        answer_and_numbers[i] = specific_action_one_number(actions_one_number[order[i]], answer_and_numbers[i])
        if answer_and_numbers[i] == -1:
            mistakes.append(i)
    answer = specific_action_two_numbers(action_two_numbers, answer_and_numbers[1], answer_and_numbers[2])
    if answer == -1:
        mistakes.append(10)

    if not mistakes and answer == answer_and_numbers[0]:
        print('Данный способ является решением')
        return True
    elif not mistakes:
        print('Неверное решение. Попробуйте снова')
        return False
    else:
        for i in range(len(mistakes)):
            if mistakes[i] < 10:
                print('Неверная операция над разрядом ', answer_about_mistake[mistakes[i]], '. Попробуйте снова', sep = '')
            else:
                print('Неверная операция над числами. Попробуйте снова')
        return False