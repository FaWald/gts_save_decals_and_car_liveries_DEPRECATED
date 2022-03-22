import sqlite3
import time


def print_hi(name):  # simple code to test
    print(f'Hi, {name}')


def write_file_array_input(file, data):
    for d in data:
        file.write(d + ";")
    file.write(",")
    pass


def create_table(db, name):
    create_table_execute = "CREATE TABLE IF NOT EXISTS " + name + "(" + "id integer PRIMARY KEY," + "picture_links text NOT NULL," + "teaser_text text," + "hashtags text" + ");"
    print(create_table_execute)
    db_cursor = db.cursor()
    db_cursor.execute(create_table_execute)
    print("Create Standard Table Done")

    pass


def connection_database(path):
    """ create a database connection to a SQLite database """
    db = sqlite3.connect(path + str(uts()) + ".db")
    print(sqlite3.version)
    return db


def uts():
    now = int(time.time())
    print(now)
    return now


def insert_data(db, data, column_name):
    values = " "
    for d in data:
        print(d)
        values.join(str(d))
    print("Values: "+values)
    pass


if __name__ == '__main__':
    print_hi('SQL-Connection')
    path = "output-files/"
    db = connection_database(path)
    name = ""
    create_table(db, "test")
    data = ["test", "test", "test"]
    column_name = "picture_links"
    insert_data(db, data, column_name)
