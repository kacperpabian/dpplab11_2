import sqlite3


class DBInterface:
    def __init__(self):
        self.createTable()

    def createTable(self):
        conn = sqlite3.connect('plannerDB2.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS
                  events(id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name text, date DATE, desc text)''')
        conn.commit()
        conn.close()

    def dbToList(self):
        conn = sqlite3.connect('plannerDB2.db')
        c = conn.cursor()
        list = c.execute('SELECT * FROM events').fetchall()
        conn.commit()
        conn.close()
        return list

    def selectTable(self):
        conn = sqlite3.connect('plannerDB2.db')
        c = conn.cursor()
        c.execute("INSERT INTO events (name, date, desc, cycl)"
                  " VALUES ('dziaga', '2018-5-28', 'granie w noge')")
        for row in c.execute('SELECT * FROM events'):
            print(row)
        conn.commit()
        conn.close()

    def deleteRow(self, id):
        conn = sqlite3.connect('plannerDB2.db')
        c = conn.cursor()
        c.execute("DELETE FROM events WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def addEvent(self, name, date, desc):
        conn = sqlite3.connect('plannerDB2.db')
        c = conn.cursor()
        c.execute("INSERT INTO events (name, date, desc)"
                  " VALUES (?, ?, ?)", (name, date, desc))
        for row in c.execute('SELECT * FROM events'):
            print(row)
        conn.commit()
        conn.close()
