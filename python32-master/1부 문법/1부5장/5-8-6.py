# -*- coding: cp949 -*-
class Tiger:
    def Jump(self):
        print("ȣ����ó�� �ָ� �����ϱ�")

class Lion:
    def Bite(self):
        print("����ó�� ���Կ� �ܲ��ϱ�")

class Liger(Tiger, Lion):	# ��ӹ��� Ŭ������
    def Play(self):
        print("���̰Ÿ��� ������� ����ְ� ���")
