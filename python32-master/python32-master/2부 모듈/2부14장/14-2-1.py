# -*- coding: cp949 -*-
import sqlite3

con = sqlite3.connect(":memory:")

with open('script.txt') as f:	# script.txt���� SQL ������ ����
	SQLScript = f.read()

cur = con.cursor()
cur.executescript(SQLScript)
