# -*- coding: cp949 -*-
class Tiger:
    def Jump(self):
        print("ȣ����ó�� �ָ� �����ϱ�")
    def Cry(self):
        print("ȣ����: ����~")

class Lion:
    def Bite(self):
        print("����ó�� ���Կ� �ܲ��ϱ�")
    def Cry(self):
        print("����: ������~")
    

class Liger(Tiger, Lion):
    def Play(self):
        print("���̰Ÿ��� ������� ����ְ� ���")
