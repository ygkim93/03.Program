# -*- coding: cp949 -*-
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE PhoneBook(Name text, Age integer);")
list = (('Tom', 24),('Derick',30), ('Peter',53), ('Jane',29))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", list)

cur.execute("SELECT length(Name), upper(Name), lower(Name) FROM PhoneBook")    # ���ڿ� ����, �빮��, �ҹ���
print("== length(), upper(), lower() ==")
print([r for r in cur])

cur.execute("SELECT max(Age), min(Age), sum(Age) FROM PhoneBook")     # �ִ밪, �ּҰ�, ����
print("== max(), min(), sum() ==")
print([r for r in cur])

cur.execute("SELECT count(*), random(*) FROM PhoneBook")              # ���ڵ� ����, ������ ��
print("== count(*), random(*) ==")
print([r for r in cur])
