import mysql.connector as mc

user = "root"
password = "root"
global db
global sql
db = mc.connect(host="localhost", user=user, password=password)
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
    try:
        sql.execute("CREATE DATABASE "+dbName)
        return 'ok'
    except mc.errors.ProgrammingError:
        return 'inputError'
    except mc.errors.DatabaseError:
        return 'databaseExists'
    except:
        return 'unknownError'


def selectDatabase(dbName):
    sql.execute("USE "+dbName)


constraints = ["NOT NULL", "DEFAULT", "UNIQUE",
               "CHECK", "Primary Key", "Foreign Key"]
colData = [{"cname": "Sno", "dtype": "int"}, {"cname": "name",
                                              "dtype": "varchar(20)"}, {"cname": "marks", "dtype": "int"},]


def createCol(colData):
    # print(colData["cname"])
    col = f'''{colData["cname"]} {colData["dtype"]},'''
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
    command = f'''create table {tbName}('''
    for i in rows:
        d = createCol(i)
        command = command+d
        # print(command)
        # print(d)
    # command = command.replace('),', ');')
    # print(command)
    # command = command.replace(');', '),',
    #                           (getOccurence_countOf(');', command)))
    command = command[:-1]
    command = command+");"
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


def arrangeColumns(columns):
    val = ''
    for i in columns:
        val += i+','
    return val


def formatRows(data):
    retVal = '('
    for i, d in enumerate(data):
        d = f"'{d}'"
        retVal += d
        if (i+1) != len(data):
            retVal += ','
    retVal += '),'
    return retVal


def insertValues(tbName, values=[], columns=[]):
    command = f'''insert into {tbName} {
        arrangeColumns(columns)} values '''
    augm = "("
    for i in range(len(values[0])):
        augm += f"%s,"
    augm = augm[0:-1]
    augm += ")"
    command += augm
    # for i in values:
    #     command += str(formatRows(i))
    # command = command[:-1]
    # command += ';'
    # print(command)
    sql.executemany(command, values)
    tbList = sql.fetchall()
    print(tbList)
    db.commit()
    print("1 record inserted, ID:", sql.lastrowid)


def checkInput(inputData):
    data = ''
    error = ''
    try:
        data = int(inputData)
        error = "Input should be alphanumeric"
        print("Data Error")
    except ValueError:
        print("OK")
        return inputData
    except:
        error = 'Unknown Error!'
