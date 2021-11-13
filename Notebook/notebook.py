from notes import Notes

class Notebook:
    def __init__(self):
        self.notes_list = []
        # self.notes_list.append(Notes(memo, tags))

    def new_note(self, memo, tags=''):
        self.notes_list.append(Notes(memo, tags))

    def modify_memo(self, noteid, new_memo):
        for note in self.notes_list:
            if note.id == int(noteid):
                note.memo = new_memo
                return True

    def modify_tag(self, noteid, new_tag):
        for note in self.notes_list:
            if note.id == int(noteid):
                note.tags = new_tag
                return True

    def search(self, filter_text):
        searched_note = [(note.id, note.memo, note.tags) for note in self.notes_list if note.match_string(filter_text)]
        if len(searched_note) > 0:
            return f"Found String at note  : {searched_note}"
        else:
            return "Not found in any notes"

    def get_note_byid(self, id):
        return [f"{note.memo}, {note.tags}" for note in self.notes_list if id == note.id]

    def delete_note_byid(self, id):
        for note in self.notes_list:
            temp_note = f"{note.memo},{note.tags}"
            if id == note.id:
                self.notes_list.remove(note)
        return temp_note


if __name__ == "__main__":
    notebook1 = Notebook()
    notebook1.new_note("read a paper", "sch")

    notebook2 = Notebook()
    notebook2.new_note("buy some water", "hom")

    print(f"notebook 1 id: {notebook1.notes_list[0].id}")
    print(f"notebook 1 memo: {notebook1.notes_list[0].memo}")
    notebook1.modify_memo(1, "read a book")
    print(f"notebook 1 modified memo: {notebook1.notes_list[0].memo}")
    print(notebook1.search("book"))

    print(f"notebook 2 id: {notebook2.notes_list[0].id}")
    print(f"notebook 2 memo: {notebook2.notes_list[0].memo}")



