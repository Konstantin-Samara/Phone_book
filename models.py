from random import randint
import csv
import controller
# ф-я генерирует заданное число случайных контактов
def get_random_phone_book(num) :
    list_names = ['Иван','Петр','Федор','Степан','Владимир','Павел','Николай',\
        'Сергей','Дмитрий','Виктор','Никанор','Евгений','Василий','Антон','Андрей',\
            'Алексей','Константин','Юрий',]
    list_father_names = ['Иванович','Петрович','Федорович','Степанович','Владимирович','Павлович','Николаевич',\
        'Сергеевич','Дмитриевич','Викторович','Никанорович','Евгеньевич','Васильевич','Антонович','Андреевич',\
            'Алексеевич','Константинович','Юрьевич',]
    list_familias = ['Иванов','Петров','Федоров','Степанов','Владимиров','Павлов','Николаев',\
        'Сергеев','Дмитриев','Викторов','Никаноров','Женин','Васильев','Антонов','Андреев',\
            'Алексеев','Константинов','Юрьев',]
    main_list_person = []
    message = 'Комментарий '
    for i in range(num) :
        list_person_phones = [str(randint(1000000000,9999999999)),str(randint(1000000000,9999999999))]
        main_list_person.append(['0', list_familias[randint(0,len(list_familias)-1)],\
            list_names[randint(0,len(list_names)-1)], \
                list_father_names[randint(0,len(list_father_names)-1)], \
                    list_person_phones, message+str(i+1)])
    main_list_person = sorted(main_list_person, key=lambda x:x[1])
    for i in range(num) : main_list_person[i][0] = str(i+1)
    main_list_person = do_actual_list(main_list_person)
    return main_list_person
# ф-я сохраняет актуальный список в формате .txt
def write_phone_book_to_txt(main_list_person) :                      
    with open('book.txt','w') as data :
        for i in range(len(main_list_person)) :
            data.writelines(str(i+1)+'\n')
            data.writelines(main_list_person[i][1]+'\n')
            data.writelines(main_list_person[i][2]+'\n')
            data.writelines(main_list_person[i][3]+'\n')        
            for n in range(len(main_list_person[i][4])) : 
                data.writelines(main_list_person[i][4][n]+',')
            data.writelines('\n')
            data.writelines(main_list_person[i][5]+'\n')
    return 
# ф-я сохраняет актуальный список в формате .csv
def write_phone_book_to_csv(list) : 
    with open("book.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ';',lineterminator="\n")
        for i in range(len(list)) :
            file_writer.writerow(str(i+1))
            for n in range(1,6) : file_writer.writerow(list[i][n])
    return
# ф-я импортирует и возвращает в качестве актуального, список из формата .csv
def get_phone_book_from_csv() :
    controller.actual_list_txt = False
    main_list_person = []
    readed_list = []    
    with open("book.csv", encoding='utf-8') as data:
        file_reader = csv.reader(data)
        for row in file_reader:
            str1 = ''
            for i in range(len(row)) : str1+=row[i]
            readed_list.append(str1)
    for i in range(0,int(len(readed_list)),6) :
        main_list_person.append([readed_list[i].replace(";", ""),\
            readed_list[i+1].replace(";", ""),readed_list[i+2].replace(";", ""),\
                readed_list[i+3].replace(";", ""),readed_list[i+4].split(';')\
                    ,readed_list[i+5].replace(";", "")])
    return main_list_person
# ф-я импортирует и возвращает в качестве актуального, список из формата .txt
def get_phone_book_from_txt() :
    main_list_person = []
    readed_list = []
    with open('book.txt','r') as data :
        for line in data : readed_list.append(line.strip())
    for i in range(0,int(len(readed_list)),6) : main_list_person.append(\
        [readed_list[i],readed_list[i+1],readed_list[i+2],\
            readed_list[i+3],readed_list[i+4][:-1].split(','),readed_list[i+5]])
    return main_list_person
# ф-я осуществляет форматированный вывод актуального списка на экран
def print_all_list(main_list_person) :
    print('СПИСОК КОНТАКТОВ :')
    for i in range(len(main_list_person)) :
        print(main_list_person[i][0] + '. ' + main_list_person[i][1]\
             + ' ' + main_list_person[i][2] + ' ' + main_list_person[i][3], end = ', тел.: ')
        for n in range(0,len(main_list_person[i][4])) : 
            print(main_list_person[i][4][n], end = ', ')
        print(main_list_person[i][5])
    return
# ф-я удаляет выбранный контакт из актуального списка
def del_contact(num,list) :
    del list[num-1]
    print('Контакт N',num, 'удален.')
    list = do_actual_list(list)
    return list
# ф-я добавляет новый контакт к актуальному списку
def add_contact(new_person,list) :
    list.append(new_person)
    list = sorted(list, key=lambda x:x[1])
    for i in range(len(list)) : list[i][0] = str(i+1)
    list = do_actual_list(list)
    return list
# ф-я заменяет существующий контакт (на сформированный в UI-edit_menu1) в актуальном списке
def edit_contact(edit_person,list) :
    list[int(edit_person[0])-1] = edit_person
    list = sorted(list, key=lambda x:x[1])
    for i in range(len(list)) : list[i][0] = str(i+1)
    list = do_actual_list(list)
    return list
# актуализирует текущий список через сохранение (формат в зависимости от значения 
# global-actual_list_txt) и прочтение. При сохранении переприсваиваются порядковые номера
# контактов, чтобы при дальнейших операциях соответствовать индексам. Используется после 
# генерации случайного списка, добавления, удаления, редактирования контакта.
def do_actual_list(list) :
    if controller.actual_list_txt :
        write_phone_book_to_txt(list)
        list = get_phone_book_from_txt()
    else :
        write_phone_book_to_csv(list)
        list = get_phone_book_from_csv()
    return list
