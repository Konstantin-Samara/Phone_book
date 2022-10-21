# ф-я осуществляет пользовательский ввод с консоли и "защита от дурака"
def my_input(str,n1,n2) :
    while True:
        try:
            select=int(input(str))
            if n1<=select<=n2 : break
            else : print("Вы ввели неправильное число - попробуйте еще раз.")
        except ValueError : print("Вы ввели не число - попробуйте еще раз.")
    return select
# ф-я возвращает в controller выбор пользователя из главного меню для последующего ветвления 
def main_menu() :
    print('\nМЕНЮ')
    print('1. Смотреть весь справочник')
    print('2. Добавить контакт')
    print('3. Удалить контакт')
    print('4. Редактировать контакт')
    print('5. Cгенерировать RANDOM-ный список контактов')
    print('6. Экспорт списка контактов в CSV-файл')
    print('7. Импорт списка контактов из CSV-файла')
    print('8. Завершить')
    return my_input('Выберите пункт меню (1-8) : ',1,8)
# ф-я возвращает в controller выбор пользователя номера(индекс+1) контакта для удаления
def del_menu(num) :
    return my_input('Введите порядковый номер удаляемого контакта : ',1,num)
# ф-я возвращает в controller выбор пользователя номера(индекс+1) контакта для редактирования
def edit_menu(num) :
    return my_input('Введите порядковый номер редактируемого контакта : ',1,num)
# ф-я возвращает в controller выбранного кол-ва контактов для составления Random - списка
def rnd_menu() :
    return my_input('Введите кол-во RANDOM-ных контактов : ',1,1000000)
# ф-я возвращает в controller добавленный элемент списка контактов
def add_menu(num) :
    i = 1
    str1 = '0'
    new_person = []
    phones = []
    familia = input('Введите фамилию : ')
    name = input('Введите имя : ') 
    father_name = input('Введите отчество : ')
    while str1!='' :
        str1 = input('Введите '+str(i)+'-й номер телефона ("Enter" - закончить): ')
        if str1!='' : 
            phones.append(str1)
            i+=1
    comment = input('Введите комментарий : ')
    new_person = [str(num+1), familia, name, father_name, phones, comment]
    return new_person
# ф-я возвращает в controller отредактированный элемент списка контактов 
def edit_menu1(edit_person) :
    my_select = 0
    my_select1 = 0
    phones = []
    familia = edit_person[1]
    name = edit_person[2]
    father_name = edit_person[3]
    phones = edit_person[4]
    comment = edit_person[5]
    while my_select!=6 :
        str1 = ''
        print ('Редактируемый контакт N '+edit_person[0])
        print ('1. Фамилия : '+edit_person[1])
        print ('2. Имя : '+edit_person[2])
        print ('3. Отчество : '+edit_person[3])
        print ('4. Телефон : ', end = '')
        for i in range (0,len(edit_person[4])) : str1=str1+edit_person[4][i]+', '
        print(str1[:-2])
        print ('5. Комментарий : '+edit_person[5])
        print ('6. Завершить редактирование')
        my_select = my_input('Введите номер поля для редактирования : ',1,6)
        if my_select==1 : 
            familia = input('Введите новую фамилию, взамен старой "'+edit_person[1]+'" : ')
        elif my_select==2 : 
            name = input('Введите новое имя, взамен старого "'+edit_person[2]+'" : ')
        elif my_select==3 : 
            father_name = input('Введите новое отчество, взамен старого "'+edit_person[3]+'" : ')  
        elif my_select==5 : 
            comment = input('Введите новый комментарий, взамен старого "'+edit_person[5]+'" : ')
        elif my_select==4 :
            my_select1 = my_input('1 - добавить номер / 2 - удалить номер : ',1,2)
            if my_select1==1 : phones.append(input('Введите добавляемый номер : '))
            else : 
                print('НОМЕРА ТЕЛЕФОНОВ КОНТАКТА N '+edit_person[0]+' :')
                for i in range(len(phones)) : print(str(i+1)+'. '+edit_person[4][i])
                del phones[my_input('Выберите номер для удаления : ',1,len(phones))-1]
        edit_person = [edit_person[0],familia,name,father_name,phones,comment]
    return edit_person

