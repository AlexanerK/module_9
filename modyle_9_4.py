from random import choice, random

first = 'Мама мыла раму'
second = 'Рамена мало было'

func_lamba = list(map(lambda x,y: x == y,first,second))
print(func_lamba)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with (open(file_name, "w", encoding='utf8') as file):
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything



write = get_advanced_writer('example.txt')
a = write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        random_word = choice(self.words)
        return random_word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
