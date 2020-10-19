# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, расположенных по возрастанию.
# Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказки: Каждый следующий случайный бочонок из мешка удобно получать с помощью функции-генератора. Для работы
# с псевдослучайными числами удобно использовать модуль random: http://docs.python.org/3/library/random.html

import random


class Card:
    def __init__(self):
        self.numbers = []
        while len(self.numbers) < 15:
            self.get_new_num(self.numbers, 3)
        self.numbers.sort()
        self._str = self._card_to_string()

    def __str__(self):
        return self._str

    def _card_to_string(self):
        tmp_list = ['-------------------------------']
        for j in range(3):
            tmp_dict = {i // 10: i for i in self.numbers if self.numbers.index(i) % 3 == j}
            if tmp_dict.get(9) is not None:
                tmp_dict[8] = tmp_dict.pop(9)
            for i in range(9):
                tmp_dict[i] = f'  ' if tmp_dict.get(i) is None else f'{tmp_dict[i]: 2}'
            tmp_list.append(' '.join([tmp_dict[i] for i in range(9)]) + ' ')
        tmp_list.append('-------------------------------')
        return '\n'.join(tmp_list)

    @staticmethod
    def get_new_num(my_list, max_counter=10):
        while True:
            n = random.randint(1, 90)
            if n not in my_list and [i // 10 for i in my_list].count(n // 10) < max_counter:
                my_list.append(n)
                break
        return n

    def cross_num(self, n):
        self.numbers.remove(n)
        self._str = self._str.replace(f' {n} ', ' - ')

    @property
    def win_check(self):
        """Returns 0 if the card has won."""
        return len(self.numbers)


class Game:
    @staticmethod
    def play():
        player_card, computer_card, played_numbers = Card(), Card(), []
        while True:
            num = Card.get_new_num(played_numbers)
            print(f'Новый бочонок: {num} (осталось {90 - len(played_numbers)})'
                  f'\nPlayer card:\n{player_card}\nComputer card:\n{computer_card}')
            user_answer = input('Зачеркнуть цифру? (y/n) ')

            if num in computer_card.numbers:
                computer_card.cross_num(num)

            if ((user_answer == 'y') != (num in player_card.numbers)) or\
                    (computer_card.win_check == 0 and player_card.win_check != 0):
                print('Game over. Computer won!')
                break
            elif user_answer == 'y':
                player_card.cross_num(num)
                if player_card.win_check == 0 and computer_card.win_check == 0:
                    print("Game over. It's a draw!")
                elif player_card.win_check == 0:
                    print('Game over. Player won!')
                    break


Game.play()
