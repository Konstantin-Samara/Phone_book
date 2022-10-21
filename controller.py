import ui
import models
# ф-я осуществляет ветвление (на основе пользовательского ввода в UI) и вызов 
# соответствующих ф-й модуля controller. Актуальным списком (по умолчанию) является
# список из book.txt

def button_click() :
    main_select = 0
    main_list = []
    global actual_list_txt
    actual_list_txt = True
    while main_select!=8 :
        if actual_list_txt : main_list = models.get_phone_book_from_txt()
        main_select = ui.main_menu()
        if main_select==1 : models.print_all_list(main_list)
        elif main_select==3 : 
            main_list = models.del_contact(ui.del_menu(len(main_list)),main_list)
        elif main_select==5 : 
            main_list = models.get_random_phone_book(ui.rnd_menu())
        elif main_select==2 : 
            main_list = models.add_contact(ui.add_menu(len(main_list)), main_list)
        elif main_select==4 : main_list = models.edit_contact(\
            ui.edit_menu1(main_list[ui.edit_menu(len(main_list))-1]), main_list)
        elif main_select==6 : models.write_phone_book_to_csv(main_list)
        elif main_select==7 : main_list = models.get_phone_book_from_csv()
    return
