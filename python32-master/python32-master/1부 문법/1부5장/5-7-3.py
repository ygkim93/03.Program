# -*- coding: cp949 -*-
class Sequencer:
    def __init__(self, maxValue):       # ������ �޼ҵ�
        self.maxValue = maxValue
    def __len__(self):                  # len()ȣ���
        return self.maxValue
    def __getitem__(self, index):      # �ε����� �������� ���� ���� 
        if( 0 < index <= self.maxValue):
            return index*10
        else:
            raise IndexError("Index out of range")
    def __contains__(self, item):       # �Ҹ� ���·� �ε����� �Ѿ���� ��ȯ 
        return (0 < item <= self.maxValue)
