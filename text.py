main_menu = ['Главное меню',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

choice_main_menu = f'Выберите пункт меню ({1}-{len(main_menu)-1}): '
choice_main_menu_error = f'Нужно веести число от 1 до {len(main_menu)-1}!'

phone_book_openned_successful = 'Телефонная книга открыта успешно!'
phone_book_saved_successful = 'Телефонная книга сохранена успешно!'

empty_phone_book_error = 'Телефонная книга пуста или не открыта!'

input_new_contact = ['Введи имя контакта: ',
                     'Введи телефон контакта: ',
                     'Введи комментарий комментарий: ',]

no_changes = 'или ENTER, чтобы оставить без изменений'

edit_contact = [f'Введи новое имя ({no_changes}): ',
                f'Введи новый телефон ({no_changes}): ',
                f'Введи новый комментарий ({no_changes}): ',]

input_search_word = 'Введите слово для поиска: '

input_search_word_for_edit = 'Введите слово для поиска, который хотите изменить: '

input_id_for_edit = 'введите ID контакта, который хотите изменить: '

input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '

input_id_for_delete = 'введите ID контакта, который хотите удалить: '

exit_no_changes = 'Спасибо, до свидания'
exit_no_changes_no_confirm = 'Спасибо, до свидания! Изменения не созранены'
exit_changes = 'Были внесены изменения!'
exit_confirm = 'Сохранить? (y/n)'

def new_contact_added_successful(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'

def edit_contact_successful(name) -> str:
    return f'Контакты "{name}" успешно изменен!'

def delete_contact_successful(name) -> str:
    return f'Контакты "{name}" успешно удален!'