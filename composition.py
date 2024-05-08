from check import correct_answer
from find import find_min_answer

def collection_of_information(number: int) -> bool:
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10 
    digits = [hundreds, tens, units]
    print('Полученное число: ', *digits, sep='')
    print('Выберите, какой разряд будет итоговым ответом: \n1 - сотен, 2 - десятков, 3 - единиц.')
    print('Для выхода нажмите 0. Чтобы посмотреть решение нажмите 4')
    answer_digit = int(input())
    while answer_digit > 4 and answer_digit < 0:
            print('Неверный ввод. Попробуйте ещё раз')
            print('Выберите, какой разряд будет итоговым ответом: \n1 - сотен, 2 - десятков, 3 - единиц')
            answer_digit = int(input())
    if answer_digit == 0:
        exit()
    elif answer_digit == 4:
        find_min_answer(digits)
        return True
    else:
        i_1 = answer_digit - 1
        i_2 = abs(1 - i_1)
        i_3 = 3 - i_1 - i_2
        given_answer = digits[i_1]
        number_one_to_transform = digits[i_2]
        number_two_to_transform = digits[i_3]
        # number_two_to_transform = sum(digits) - given_answer - number_one_to_transform
        answer_and_numbers = [given_answer, number_one_to_transform, number_two_to_transform]
        order = [i_1, i_2, i_3]

        what_digit = ['сотен', 'десятков', 'единиц']
        actions_one_number = []
        for i in range(3):
            print('Выберите операцию над разрядом ', what_digit[i], ":", sep = '')
            print('1 - умножение на два, 2 - умножение на три, 3 - деление на два, 4 - деление на три, 0 - не изменять число')
            print('Если больше не собираетесь преобразовывать число выберите -1')
            print('Операция деления может быть применена над числом, только если оно делится нацело')
            answer_action = int(input())
            while answer_action > 4 and answer_action < -1:
                print('Неверный ввод. Попробуйте ещё раз')
                print('1 - умножение на два, 2 - умножение на три, 3 - деление на два, 4 - деление на три, 0 - не изменять число')
                print('Операция деления может быть применена над числом, только если оно делится нацело')
                answer_action = int(input())
            if answer_action == -1:
                while len(actions_one_number) <= 3:
                    actions_one_number.append(0)    
                break
            else:
                actions_one_number.append(answer_action)
        
        print('Выберите операцию над оставшимися числами:')
        print('1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление')
        action_two_numbers = int(input())
        while action_two_numbers > 4 and action_two_numbers < 1:
                print('Неверный ввод. Попробуйте ещё раз')
                print('1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление')
                action_two_numbers = int(input())
        if correct_answer(action_two_numbers, actions_one_number, answer_and_numbers, order):
            return True
        else:
            return False
