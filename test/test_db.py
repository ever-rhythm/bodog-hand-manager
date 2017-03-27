
import sqlite3

conn = sqlite3.connect('/Users/qinmengyao/PythonProjects/python3/git_bodog/output/hm.db')

c = conn.cursor()

print(c.execute("select * from sqlite_master").fetchall())
