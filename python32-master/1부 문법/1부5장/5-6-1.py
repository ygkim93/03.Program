# -*- coding: cp949 -*-
class CounterManager:
    insCount = 0
    def __init__(self):         # �ν��Ͻ� ��ü�� ������ Ŭ���� ������ insCount ���� ���� 
        CounterManager.insCount += 1
    def printInstaceCount():    # �ν��Ͻ� ��ü ���� ��� 
        print ("Instance Count: ", CounterManager.insCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.printInstaceCount()        # �ν��Ͻ� ���� ��� 
b.printInstaceCount()           # �Ͻ������� �ν��Ͻ� ��ü�� �ޱ� ������ Error�� �߻�
