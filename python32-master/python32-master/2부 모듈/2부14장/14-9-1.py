# -*- coding: cp949 -*-
class Point(object):   
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):             # Point ��ü�� ���� ���     
        return "Point(%f, %f)" % (self.x, self.y)

import sqlite3
def PointAdapter(point):                # Ŭ���� ��ü���� SQLite3 �Է� ������ �ڷ������� ��ȯ      
    return "%f:%f" % (point.x, point.y)

def PointConverter(s):                  # SQLite3���� ��ȸ�� ����� Ŭ���� ��ü�� ��ȯ 
    x, y = list(map(float, s.decode().split(":")))
    return Point(x, y)

sqlite3.register_adapter(Point, PointAdapter)          # Ŭ���� �̸��� ��ȯ �Լ� ���
sqlite3.register_converter("point", PointConverter)    # SQL �������� ����� �ڷ��� �̸��� ��ȯ�Լ� ���

p = Point(4, -3.2)           # �Է��� ������(���̽� Ŭ���� ��ü)
p2 = Point(-1.4, 6.2)

# �Ϲ������� ����� �ڷ������� ��ȸ�ϵ��� ����  
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test(p point)")             # point �ڷ����� �̿��Ͽ� ���̺� ����

cur.execute("insert into test values (?)", (p, ))     # point ���ڵ� �Է�
cur.execute("insert into test(p) values (?)", (p2,))

cur.execute("select p from test")    # ���̺� ��ȸ 
print([r[0] for r in cur])           
cur.close()
con.close()
