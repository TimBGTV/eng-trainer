#d = {'instread':'вместо', 'environment':'окружающаясреда', 'also':'также'}

d = {}
with open("файл.txt") as file:
    lines = file.read().splitlines()
    #print(lines)

for line in lines:
    #print(line)
    key, value = line.split(':')
    d.update({key: value})


    #for line in file:
        #key, *value = line.split("-")
        #d[key] = value

#print(d)

line = '___________________________________'

choice = input('Пройти тест - тест. Добавить слово - добавить. -----> ')


def test():
    for key, value in d.items():
        print(line)
        answer = input(f'{key} - ')
        if answer == value:
            #print(line)
            continue
        else:
            mistake = input('Ответ неверный, попробуй еще ---> ')
            if mistake == value:
                continue
            else:
                mistake = input('Ответ неверный, последняя попытка ---> ')
                if mistake == value:
                    continue
                else:
                    print('Иди повторяй.')
                    break


def refill():
    eng = input('Введите слово на английском: ')
    ru = input('Введите перевод: ')
    d[f'{eng}'] = f'{ru}'


if choice == 'тест':
    test()
if choice == 'добавить':
    refill()
else:
    print('Подумайте и приходите в другой раз!')
