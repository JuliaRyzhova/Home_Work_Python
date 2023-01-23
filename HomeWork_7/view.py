import loggs as log
import Input_data as input
import models as mod

operation = ''
phone = ''


def run():
    global phone
    operation = input.get_operation()
    log.operation_logger(operation)
    if operation == '1':
        choose_view_model = input.get_show_option()
        if choose_view_model == '4':
            mod.show_data_inline()
            log.showDB_v1_logger()
            run()
        if choose_view_model == '5':
            mod.show_data_incolumn()
            log.showDB_v2_logger()
            run()
        else:
            print('Такой операции нет. Давай попробуем еще раз!')
            run()
    if operation == '2':
        searching_req = input.get_searching_data()
        print('')
        mod.searching_contact(searching_req)
        log.search_contact_logger(searching_req)
        run()
    if operation == '3':
        surname = input.get_surname()
        log.surname_logger(surname)
        name = input.get_name()
        log.name_logger(name)
        phone = input.get_phone()
        log.phone_logger(phone)
        description = input.get_description()
        log.description_logger(description)
        lst_data = [surname, name, phone, description]
        mod.create_contact(lst_data)
        print()
        print('Новый контакт добавлен!')
        print('______________________________________')
        mod.searching_contact(phone)
        log.create_new_contact_logger(phone)
        run()
    else:
        print('Такой операции нет. Давай попробуем еще раз!')
        run()
