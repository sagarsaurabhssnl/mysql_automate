import mysql.connector as mc

global db
global sql
db = mc.connect(host="localhost", user="root", password="root")
sql = db.cursor()


def listDatabases():
    sql.execute("SHOW DATABASES;")
    dbList = sql.fetchall()
    dbArr = []
    for i in dbList:
        for j in i:
            dbArr.append(j)
    return (dbArr)


def listTables():
    sql.execute("show tables;")
    tbList = sql.fetchall()
    tbArr = []
    for i in tbList:
        for j in i:
            tbArr.append(j)
    return (tbArr)


def createDatabase(dbName):
    sql.execute("CREATE DATABASE;"+dbName)


def selectDatabase(dbName):
    sql.execute("USE "+dbName)


constraints = ["NOT NULL", "DEFAULT", "UNIQUE",
               "CHECK", "Primary Key", "Foreign Key"]
colData = [{"cname": "Sno", "dtype": "int"}, {"cname": "name",
                                              "dtype": "varchar"}, {"cname": "marks", "dtype": "int"},]


def createCol(colData):
    # print(colData["cname"])
    col = f'''({colData["cname"]} {colData["dtype"]}),'''
    return col

#  {colData["attr"] if (colData["attr") else ''}


def getOccurence_countOf(t, data):
    count = 0
    prev = ''
    for i in data:
        if prev+i == t:
            count += 1
        prev = i
    print("count"+str(count))
    return count-1


def createTable(tbName, rows=colData):
    command = f'''create table {tbName}'''
    for i in rows:
        d = createCol(i)
        command = command+d
        # print(command)
        # print(d)
    command = command.replace('),', ');')
    print(command)
    command = command.replace(');', '),',
                              (getOccurence_countOf(');', command)))
    print(command)
    try:
        sql.execute(command)
        print(command)
        return (f"Table {tbName} created")
    except:
        return ("Error")


def describeTable(tbName):
    sql.execute(F"DESC {tbName}")


def executeCommand(command):
    sql.execute(command)
