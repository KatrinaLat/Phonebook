import view
from model import PhoneBook
import text

def find_contacts(phone_book, message):
    serch_word = view.input_data(message)
    result = phone_book.find_contact(serch_word)
    view.show_contacts(result, text.find_contact_no_result(serch_word))
    return True if result else False


def start_app():
    pb = PhoneBook()
    while True:
        user_choice = view.show_main_manu()
        match user_choice:
            case 1:
                pb.open_phone_book()
                view.show_message(text.phone_book_openned_successful)
            case 2:
                pb.save_phone_book()
                view.show_message(text.phone_book_saved_successful)
                pass
            case 3:
                view.show_contacts(pb.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                pb.add_new_contact(new_contact)
                view.show_message(text.new_contact_added_successful(new_contact[0]))
            case 5:
                find_contacts(pb, text.input_search_word)
            case 6:
                if find_contacts(pb, text.input_search_word_for_edit):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = pb.edit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_successful(name))
            case 7:
                if find_contacts(pb, text.input_search_word_for_delete):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = pb.delete_contact(u_id)
                    view.show_message(text.delete_contact_successful(name))
            case 8:
                if pb.on_exit():
                    view.show_message(text.exit_changes)
                    if view.input_data(text.exit_confirm).lower() == 'y':
                        pb.save_phone_book()
                    else:
                        view.show_message(text.exit_no_changes_no_confirm)                
                else:
                    view.show_message(text.exit_no_changes)
                break
            
