import datetime
import sysconfig

last_id = 0

class Notes:

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.index = 0
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match_string(self, filter_text):
        return filter_text in self.memo or filter_text in self.tags


if __name__ == "__main__":
    note1 = Notes("Buy newspaper", "HOM")
    note2 = Notes("Read a paper", "SCH")
    print("Note 1 id: {}".format(note1.id))
    print("Note 2 id: {}".format(note2.id))

    print(note1.match_string("paper"))