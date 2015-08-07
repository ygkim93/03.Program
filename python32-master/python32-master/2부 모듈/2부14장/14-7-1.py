# -*- coding: cp949 -*-
class Average:
    def __init__(self):
        self.sum = 0          # sum, cnt�� �ʱ�ȭ
        self.cnt = 0

    def step(self, value):
        self.sum += value     # �Էµ� ���� sum�� ���ϰ�, ī��Ʈ(cnt)�� ���� 
        self.cnt += 1

    def finalize(self):
        return self.sum / self.cnt    # ����� ��ȯ

import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE User(Name text, Age int);")
list = (('Tom', '16'),
 ('DSP', '33'),
('Derick', '25'))
cur.executemany("INSERT INTO User VALUES(?, ?);", list)   

con.create_aggregate("avg", 1, Average)        # Average Ŭ������ ����� ���� �����Լ��� ���

cur.execute("SELECT avg(Age) FROM User")       # ���ǽ� ������ ����� ���� ���� �Լ��� ���
print(cur.fetchone()[0])                       # ��� ���: 24.6666666667 
