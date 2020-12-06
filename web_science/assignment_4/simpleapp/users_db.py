import sqlite3

users = [
    ["Zoe", "douglas@gmail.com"],
    ["Audrey", "audrey_burton@gmail.com"],
    ["John", "langstaff@gmail.com"]
]


def init_db():
    with sqlite3.connect('database.db', uri=True) as conn:
        conn.execute('DROP TABLE IF EXISTS clients')
        print("Dropped the table")
        conn.execute('CREATE TABLE IF NOT EXISTS  clients (name TEXT, email TEXT)')
        print("Created the table.")
        for user in users:
            add_user(user)


def is_user_registered(user):
    result = None
    with sqlite3.connect('database.db', uri=True) as conn:
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM clients WHERE (name='{user[0]}') AND (email='{user[1]}')")
        result = cur.fetchone()
    return False if result is None else True

def count_users():
    with sqlite3.connect('database.db', uri=True) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from clients")
        rows = cur.fetchall();
        return len(rows)


def add_user(user):
    _name = user[0]
    _email = user[1]
    with sqlite3.connect('database.db', uri=True) as conn:
        try:
            cur = conn.cursor()
            statement = "INSERT INTO clients (name,email) VALUES(?, ?)"
            cur.execute(statement, (_name, _email))
            conn.commit()
            print("Record successfully added")
        except:
            conn.rollback()
            print("error in insert operation")
