from copy import deepcopy

class PhoneBook:
    def __init__(self, path='phone.txt', separator=';'):
        self.phone_book = {}
        self.path = path
        self.SEPARATOR = separator
        self.original_phone_book = self.phone_book
        
    def copy_org_phone_book(self):
        self.original_phone_book = deepcopy(self.phone_book)

    def open_phone_book(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for u_id, contact in enumerate(data, 1):
            self.phone_book[u_id] = contact.strip().split(self.SEPARATOR)
        self.copy_org_phone_book()

    def save_phone_book(self):
        data = []
        for contact in self.phone_book.values():
            data.append(self.SEPARATOR.join(contact))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.copy_org_phone_book
            
    def _next_id(self):
        return max(self.phone_book) + 1 if self.phone_book else 1

    def add_new_contact(self, new_contact: list[str]):
        self.phone_book[self._next_id()] = new_contact
            
    def find_contact(self, serch_word: str) -> dict[int, list[str]]:
        result = {}
        for u_id, contact in self.phone_book.items():
            if serch_word.lower() in ' '.join(contact).lower():
                result[u_id] = contact
        return result

    def edit_contact(self, u_id: int, edited_contact: list[str]) -> str:
        current_contact = self.phone_book[u_id]
        for i in range(len(current_contact)):
            current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
        self.phone_book[u_id] = current_contact
        return current_contact[0]

    def delete_contact(self, u_id: int) -> str:
        return self.phone_book.pop(u_id)[0]
    def on_exit(self):
        if self.phone_book == self.original_phone_book:
            return False
        return True