# -*- coding: cp949 -*-
class CounterManager:
    __insCount = 0			# �̸� ������ ���Ͽ� '__'�� ������ �տ� ��� 
    def __init__(self):    
        CounterManager.__insCount += 1
    def staticPrintCount():
        print ("Instance Count: %d" % CounterManager.__insCount)  # Ŭ���� ���ο��� ���� ������ �̸��� �����ϰ� ��� ����
    SPrintCount = staticmethod(staticPrintCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.SPrintCount()
