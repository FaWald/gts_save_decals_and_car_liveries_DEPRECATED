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
    create_table_execute = "CREATE TABLE IF NOT EXISTS " + name + "(" + "id integer PRIMARY KEY," + "picture_links text NOT NULL," + "teaser_text text," + "hashtags_and_keywords text" + ");"
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


def insert_data(db, data, name, column_name):
    db_cursor = db.cursor()
    for d in data:
        print("Data: " + d)
        insert_into_cmd = "INSERT INTO " + name + " (" + column_name + ") VALUES('" + d + "');"
        print(insert_into_cmd)
        db_cursor.execute(insert_into_cmd)
    db.commit()
    db.close()
    pass


if __name__ == '__main__':
    print_hi('SQL-Connection')
    path = "output-files/"
    db = connection_database(path)
    name = "test"
    create_table(db, name)
    data = ["test1", "test2", "test3"]
    column_name = "picture_links"
    insert_data(db, data, name ,column_name)
