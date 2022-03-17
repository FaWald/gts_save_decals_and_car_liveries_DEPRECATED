import time

#columns = []
arrRow = []
columnCounter = 0;


def print_hi(name):  # simple code to test
    print(f'Hi, {name}')


def uts():
    now = int(time.time())
    print(now)
    return now


uts_now = str(uts())


def create_file(path):
    uts()
    file = open(path + uts_now + ".csv", "x")
    file.close()
    file = open(path + uts_now + ".csv", "w")
    return file


def write_file(file, column, row, inhalt):
    file.write(inhalt)
    pass


def read_file():
    return 0


def collectData(dataArray):
    arrColumn = dataArray






    pass


if __name__ == '__main__':
    print_hi('CSV-Connection')
    path = "output-files/"
    file = create_file(path)
    column = 1
    row = 1
    exampleData = "Test;test;test"
    exampleArray = ["Test1", "Test2", "Test3"]
    collectData(exampleArray)
    write_file(file, column, row, exampleData)

    read_file()

