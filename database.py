import sqlite3

class PeopleDatabase:
    def __init__(self):
        self.connect = sqlite3.connect("PeopleDatabase.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS people
                            (creator text, name text, surename text, birthDay int,
                            birthMonth int, birthYear int, gender text)""")
        self.connect.commit()

    def __delete__(self):
        self.connect.close()

    def add_entry(self, entry):
        self.cursor.execute('INSERT INTO people VALUES (?,?,?,?,?,?,?)', entry)
        self.connect.commit()

    def add_entry_list(self, entries):
        self.cursor.executemany('INSERT INTO people VALUES (?,?,?,?,?,?,?)', entries)
        self.connect.commit()

    def get_entry(self, id):
        return [i for i in self.cursor.execute('SELECT * FROM people WHERE rowid=?', (id,))][0]

    def get_created_entries(self, creator):
        return self.cursor.execute('SELECT * FROM people WHERE creator=?', (creator,))

    def get_all_entries(self):
        return self.cursor.execute('SELECT rowid, * FROM people ORDER BY surename')

    def del_entry(self, id):
        self.cursor.execute('DELETE FROM people WHERE rowid=?', (id,))
        self.connect.commit()

    def del_all_entries(self):
        self.cursor.execute('DELETE FROM people WHERE 1=1')
        self.connect.commit()
