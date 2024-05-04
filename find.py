from check import specific_action_two_numbers, specific_action_one_number

def find_all_answers(digits: list) -> None:
    transform_1, transform_2, transform_3 = 0,0,0
    for i_1 in range(3):
        answer = digits[i_1]
        i_2 = abs(1 - i_1)
        i_3 = 3 - i_1 - i_2
        number_2 = digits[i_2]
        number_3 = digits[i_3]
        for action in range(1,5):
            while True:
                new_answer = specific_action_one_number(transform_1, answer)
                new_number_2 = specific_action_one_number(transform_2, number_2)
                new_number_3 = specific_action_one_number(transform_3, number_3)
                result = specific_action_two_numbers(action, new_number_2, new_number_3)
                if result == new_answer and (new_answer != -1 and new_number_2 != -1 and new_number_3 != -1):
                    what_digit = ['сотен', 'десятков', 'единиц']
                    what_transform = ['не изменен', 'умножен на два', 'умножен на три', 'поделен на два', 'поделен на три']
                    what_action = ['сложения', 'вычитания', 'умножения', 'деления']
                    what_action_symbols = ['+', '-', '*', ':']
                    for j in range(3):
                        if j == i_1:
                            print('Разряд', what_digit[j] , 'был', what_transform[transform_1])
                        elif j == i_2:
                            print('Разряд', what_digit[j] , 'был', what_transform[transform_2])
                        elif j == i_3:
                            print('Разряд', what_digit[j] , 'был', what_transform[transform_3])
                    print('Из разрядов', what_digit[i_2], 'и', what_digit[i_3], 'был получен разряд', what_digit[i_1], 
                          'при помощи', what_action[action-1])
                    print(max(new_number_2, new_number_3), what_action_symbols[action-1] , min(new_number_2, new_number_3), '=', new_answer)
                    print('')
                transform_1 += 1
                if transform_1 > 4:
                    transform_1 = 0
                    transform_2 += 1
                    if transform_2 > 4:
                        transform_2 = 0
                        transform_3 += 1
                        if transform_3 > 4:
                            transform_1 = 0
                            transform_2 = 0
                            transform_3 = 0
                            break
# find_all_answers([1,6,4])

def find_min_answer(digits: list) -> None:
    transform_1, transform_2, transform_3 = 0,0,0
    best_weight = 105
    best_transform = [0,0,0]
    best_action = 0
    weight_transform = [0, 10, 30, 12, 32]
    weight_action = [1, 2, 5, 7]
    best_numbers_index = [0,0]
    best_answer_index = 0
    for i_1 in range(3):
        answer = digits[i_1]
        i_2 = abs(1 - i_1)
        i_3 = 3 - i_1 - i_2
        number_2 = digits[i_2]
        number_3 = digits[i_3]
        for action in range(1,5):
            while True:
                new_answer = specific_action_one_number(transform_1, answer)
                new_number_2 = specific_action_one_number(transform_2, number_2)
                new_number_3 = specific_action_one_number(transform_3, number_3)
                result = specific_action_two_numbers(action, new_number_2, new_number_3)
                if result == new_answer and (new_answer != -1 and new_number_2 != -1 and new_number_3 != -1):
                    weight_new_answer = (weight_transform[transform_1] + weight_transform[transform_2] + weight_transform[transform_3] + 
                                         weight_action[action-1])
                    if weight_new_answer < best_weight:
                        best_weight = weight_new_answer
                        for j in range(3):
                            if j == i_1:
                                best_transform[j] = transform_1
                            elif j == i_2:
                                best_transform[j] = transform_2
                            elif j == i_3:
                                best_transform[j] = transform_3
                        best_action = action
                        best_answer_index = i_1
                        best_numbers_index = [i_2, i_3]
                        best_answer = new_answer
                        best_numbers = [max(number_2, number_3), min(number_2, number_3)]
                transform_1 += 1
                if transform_1 > 4:
                    transform_1 = 0
                    transform_2 += 1
                    if transform_2 > 4:
                        transform_2 = 0
                        transform_3 += 1
                        if transform_3 > 4:
                            transform_1 = 0
                            transform_2 = 0
                            transform_3 = 0
                            break
    if best_action == 0:
        print('Решений нет')
    else:
        what_digit = ['сотен', 'десятков', 'единиц']
        what_transform = ['не изменен', 'умножен на два', 'умножен на три', 'поделен на два', 'поделен на три']
        what_action = ['сложения', 'вычитания', 'умножения', 'деления']
        what_action_symbols = ['+', '-', '*', ':']
        for j in range(3):
            print('Разряд', what_digit[j] , 'был', what_transform[best_transform[j]])
        print('Из разрядов', what_digit[best_numbers_index[0]], 'и', what_digit[best_numbers_index[1]], 
                'был получен разряд', what_digit[best_answer_index], 'при помощи', what_action[best_action-1])
        print(best_numbers[0], what_action_symbols[best_action-1], best_numbers[1], '=', best_answer)
        print(' ')
# find_min_answer([7,8,9])