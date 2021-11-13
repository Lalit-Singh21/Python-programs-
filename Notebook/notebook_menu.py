import sys
from notebook import Notebook

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.search_note_byid,
            "6": self.delete_note,
            "7": self.quit_program,
        }

    def display_menu(self):
        print("""
        1. Show all notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. search note by id
        6. delete note
        7. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option:")
            action = self.choices.get(choice) # calling function from dictionary
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")
                continue

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes_list
        if len(notes) == 0:
            print("No notes added")
        for note in notes:
            print(f"ID: {note.id} Memo: {note.memo} Tag: {note.tags}")

    def search_notes(self):
        filter_string = input("search for: ")
        if len(self.notebook.notes_list) == 0:
            print("No Notes Added")
        else:
            notes = self.notebook.search(filter_string)
            print(notes)

    def add_note(self):
        memo = input("enter a memo:")
        tag = input("enter a tag:")
        self.notebook.new_note(memo, tag)
        print("Note added successfully")

    def get_id(self):
        while 1:
            try:
                id = int(input("Enter Note ID:"))
                return id
            except ValueError as v:
                print("Enter an integer value")
                continue

    def modify_note(self):
        id = self.get_id()
        id_present = [id for notes in self.notebook.notes_list if id == notes.id]
        if len(id_present) > 0:
            memo = input("Enter note memo:")
            tags = input("Enter note tags:")
            memo_modified = self.notebook.modify_memo(id, memo)
            tag_modified = self.notebook.modify_tag(id, tags)
            if memo_modified and tag_modified:
                print("Note modified successfully")
        else:
            print("ID not Present, see list below: ")
            self.show_notes()

    def search_note_byid(self):
        id = self.get_id()
        id_present = [notes for notes in self.notebook.notes_list if id == notes.id]
        if len(id_present) > 0:
            note_memo_tag = self.notebook.get_note_byid(id)
            print(f"Note on ID {id}: {note_memo_tag}")
        else:
            print("ID not Present, see list below: ")
            self.show_notes()

    def delete_note(self):
        id = self.get_id()
        id_present = [notes for notes in self.notebook.notes_list if id == notes.id]
        if len(id_present) > 0:
            note_memo_tag = self.notebook.delete_note_byid(id)
            print(f"Deleting note {id}: {note_memo_tag}")
        else:
            print("ID not Present, see list below: ")
            self.show_notes()

    def quit_program(self):
        print("Good day!")
        sys.exit(0)

if __name__ == "__main__":
    menu1 = Menu()
    menu1.run()