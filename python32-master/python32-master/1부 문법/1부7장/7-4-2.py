# -*- coding: cp949 -*-
def RaiseErrorFunc():
    raise NameError("NameError�� ����")

def PropagateError():
    try:
        RaiseErrorFunc()                        
    except:
        print("�������� ������ ���� �� �޼����� ��µ˴ϴ�.")
        raise     # �߻��� ������ ������ ���� 

PropagateError()
