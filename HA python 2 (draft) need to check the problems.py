import csv
def init_arr():
    """
    Данная функция создает изначальный массив массивов, в котором храняться все данные.
    """
    gen_arr = []
    arr = []
    with open('Corp_Summary.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            gen_arr.append(' '.join(row))
        for line in gen_arr:
            arr.append(line.split(';'))
    return arr

def depart_teams(arr):
    """
    Данная функция получает на вход массив массивов, в котором записаны все данные.
    Мы проходим по всем данным и собираем информацию о существующих департаментах и работающих в них командах.
    В выводе будет словарь, в котором ключами являются департаменты, а значениями - команды.
    """
    dict_d_t = {}
    for line in arr:
        if dict_d_t.get(line[1])==None:
            dict_d_t[line[1]] = set()
            dict_d_t[line[1]].add(line[2])
        else:
            dict_d_t[line[1]].add(line[2])
    print(dict_d_t)


def wages(arr):
    """
    Данная функция принимает на вход массив массивов, в котором записаны все данные.
    В результате работы функции создается запись, в которой содержатся минимальная, максимальная и средняя зарплаты по каждому департаменту.
    """
    dict_w = {}
    for line in arr:
        if line[1]!= 'Департамент':
            if dict_w.get(line[1])==None:
                dict_w[line[1]] = []
                dict_w[line[1]].append(int(line[-1]))
            else:
                dict_w[line[1]].append(int(line[-1]))
    for dep in dict_w:
        print(dep, ':', 'численность:', len(dict_w[dep]), '; минимальная заработная плата:', min(dict_w[dep]), '; максимальная заработная плата:', max(dict_w[dep]), '; средняя заработная плата:', sum(dict_w[dep])/len(dict_w[dep]), '.')
def wages_1(arr):
    """
    Данная функция принимает на вход массив массивов, в котором записаны все данные.
    Функция возвращает словарь с зарплатами по департаментам.
    """
    dict_w = {}
    for line in arr:
        if line[1]!= 'Департамент':
            if dict_w.get(line[1])==None:
                dict_w[line[1]] = []
                dict_w[line[1]].append(int(line[-1]))
            else:
                dict_w[line[1]].append(int(line[-1]))
    return dict_w
def summary(dict_w):
    """
    Данная функция принимает на вход словарь, содержащий нужные данные о зарплате.
    Функция делает запись в файле csv.
    """
    with open('Summary.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for dep in dict_w:
            writer.writerow([dep, 'минимальная заработная плата:', str(min(dict_w[dep])), 'максимальная заработная плата:', str(max(dict_w[dep])), 'средняя заработная плата:', str(sum(dict_w[dep])/len(dict_w[dep]))])
if __name__ == '__main__':
    print('Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него - 1. '
    'Вывести сводный отчёт по департаментам: название, численность, вилка зарплат в виде мин – макс, среднюю зарплату - 2. '
    'Сохранить сводный отчёт из предыдущего пункта в виде csv-файла - 3.')
    inp = input()
    if inp == '1':
        depart_teams(init_arr())
    elif inp == '2':
        wages(init_arr())
    elif inp == '3':
        summary(wages_1(init_arr()))
    else:
        print('Введено недопустимое число.')