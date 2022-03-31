import tkinter
from tkinter import ttk

import tk

import csvConnection
import seleniumConnection
import sqlConnection


def print_hi(name):
    print(f'Hi, {name}')


def test_SeleniumConnect():
    seleniumConnection.print_hi("Selenium-Connection")
    pass


def test_tkinter():
    tkinter._test()
    pass


def App_test(root):
    label1 = tkinter.Label(root, text="Hello, World", bg="green")
    label1.pack(side="top")
    label2 = tkinter.Label(root, text="Hello, World", bg="red")
    label2.pack(side="top", fill="x")
    button1 = ttk.Button(root, text="Klick Mich!")
    button1.pack(side="left")
    entry1 = ttk.Entry(root, width=40)
    entry1.pack(side="top", fill="x")
    return "test"


def App(root):
    # Username
    label1 = tkinter.Label(root, text="Username/Keyword: ")
    label1.pack(side="top", fill="x")
    entry1 = ttk.Entry(root)
    entry1.pack(side="top", fill="x")

    def PrintUsername():
        print('Username/Keyword: ' + entry1.get())
        pass

    buttonUsername = ttk.Button(root, text="Accept Username/Keyword", command=PrintUsername)
    buttonUsername.pack(side="top", fill="x")
    # DropDown Menu

    OptionList = [
        "None",
        "CarLivery",
        "HelmetLivery",
        "Decal",
        "SuitLivery"
    ]
    variable = tkinter.StringVar(root)
    variable.set(OptionList[0])

    opt = tkinter.OptionMenu(root, variable, *OptionList)
    opt.pack(side="top", fill="x")

    def callback(*args):
        print("DropDownMenu: " + variable.get())

    variable.trace("w", callback)

    # Quit Button
    buttonQuit = ttk.Button(root, text="Quit Program", command=root.destroy)
    buttonQuit.pack(side="bottom", fill="x")

    def InfoToCSV():
        print("Info to CSV")
        elementArray = InfoToConsole()
        path = "output-files/"
        file = csvConnection.create_file(path)
        csvConnection.write_file_array_input(file, elementArray)
        pass

    def InfoToSQLDB():
        print("Info to SQL-Database")
        elementArray = InfoToConsole()
        path = "output-files/"
        db = sqlConnection.connection_database(path)
        name = entry1.get()
        column_name = "picture_links"
        sqlConnection.create_table(db, name)
        sqlConnection.insert_data(db, elementArray, name, column_name)
        print("Done")

        pass

    def InfoToConsole():
        print("Info to Console")
        print("_" * 20)
        print("Username/Keyword: " + entry1.get())
        print("Livery: " + variable.get())
        url_tag = seleniumConnection.liveryToURL(variable.get())
        driver = seleniumConnection.selenium_start_driver_firefox()
        player_id = entry1.get()
        seleniumConnection.open_gts_site(driver, player_id, url_tag)
        # searched_class = seleniumConnection.liveryToHTML(variable.get())
        searched_class = "sumb"
        print("HTML-Class: " + searched_class)
        elementArray = seleniumConnection.searching_element(driver, searched_class)
        print(elementArray)
        for i in elementArray:
            print(i)

        return elementArray

    def savePics():
        pass

    # HTML to CSV
    buttonCSV = ttk.Button(root, text="Information to CSV", command=InfoToCSV)
    buttonCSV.pack(side="bottom", fill="x")
    # HTML to SQL
    buttonSQL = ttk.Button(root, text="Information to SQL-Database", command=InfoToSQLDB)
    buttonSQL.pack(side="bottom", fill="x")
    # HTML to Console
    buttonConsole = ttk.Button(root, text="Information to Console", command=InfoToConsole)
    buttonConsole.pack(side="bottom", fill="x")
    return 0


def start_tkinter():  # starting tkinter window
    root = tkinter.Tk()
    root.title("GTS-Delivery-Downloader")
    root.geometry("350x250")
    root.minsize(width=350, height=250)
    root.maxsize(width=800, height=800)
    root.resizable(width=True, height=True)
    # app_testing_tkinter = App_test(root)
    app = App(root)
    root.mainloop()
    return app


def test_CSVConnection():
    csvConnection.print_hi("CSV-Connection")
    pass


def test_SQLConnection():
    sqlConnection.print_hi("SQL-Connection")
    pass


if __name__ == '__main__':
    print_hi('GUI')
    test_SeleniumConnect()
    test_CSVConnection()
    test_SQLConnection()
    # test_tkinter()
    start_tkinter()
