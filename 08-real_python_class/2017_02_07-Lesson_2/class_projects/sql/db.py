##
# Class project 3: sqlite3
#
import sqlite3

with sqlite3.connect('calc.db') as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE calculations
        (num1 INTEGER, num2 INTEGER, operator TEXT, solution REAL)""")
    cursor.execute("""INSERT INTO calculations VALUES 9 3 'add' 12""")
