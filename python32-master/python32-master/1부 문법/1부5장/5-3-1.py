# -*- coding: cp949 -*-
str = "NOT Class Member" # ���� ����
class GString:
    str = ""             # Ŭ���� ��ü ��� ����
    def Set(self, msg):
        self.str = msg
    def Print(self):  
        print(str)       # self�� �̿��Ͽ� Class ����� �������� �ʴ� ��� 
                         # �̸��� ������ ���� ������ �����Ͽ� ���

g = GString()
g.Set("First Message")
g.Print()
