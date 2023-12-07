# import mysql.connector as mc

# mydb = mc.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )

# print(mydb)

import random


class Box:
    def __init__(this, name):
        this.name = name
        this.random = random.randint(1, 100)

    def getName(this):
        print(this.name)


b1 = Box("sagar")
b2 = Box("a")
b1.getName()
