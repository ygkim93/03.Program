# -*- coding: cp949 -*-
def RaiseErrorFunc():
    raise NameError     # ���� ������ NameError�� �߻�

try:
    RaiseErrorFunc()
except: 
    print("NameError is Catched")
