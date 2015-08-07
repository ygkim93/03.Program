# -*- coding: cp949 -*-
class CounterManager:
    insCount = 0
    def __init__(self):    
        CounterManager.insCount += 1
    def staticPrintCount():                         # ���� �޼ҵ� ����
        print ("Instance Count: ", CounterManager.insCount)
    SPrintCount = staticmethod(staticPrintCount)    # ���� �޼ҵ�� ��� 

    def classPrintCount(cls):                       # Ŭ���� �޼ҵ� ����(�Ͻ������� ù ���ڴ� Ŭ������ ����) 
        print ("Instance Count: ", cls.insCount)
    CPrintCount = classmethod(classPrintCount)      # Ŭ���� �޼ҵ�� ��� 

a, b, c = CounterManager(), CounterManager(), CounterManager()

# ���� �޼ҵ�� �ν��Ͻ� ��ü ������ ��� 
CounterManager.SPrintCount()       
b.SPrintCount()

# Ŭ���� �޼ҵ�� �ν��Ͻ� ��ü ������ ���
CounterManager.CPrintCount()
b.CPrintCount()
