import random
from lib import *


# sql = db.cursor()
# a = sql.execute("show databases")
# print(a.fetchall())


class Box:
    def __init__(this, name):
        this.name = name
        this.random = random.randint(1, 100)

    def getName(this):
        print(this.name)


# b1 = Box("sagar")
# b2 = Box("a")
# b1.getName()
colData = [{"cname": "Sno", "dtype": "int"}, {"cname": "name",
                                              "dtype": "varchar"}, {"cname": "marks", "dtype": "int"},]

print(listDatabases())
# print(createTable("afaees"))
