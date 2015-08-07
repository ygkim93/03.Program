# -*- coding: cp949 -*-
class NegativeDivisionError(Exception):   # ����� ���� ���� ����
    def __init__(self, value):
        self.value = value

def PositiveDevide(a, b):
    if(b < 0):         # ������ 0���� ���� ���, NegativeDivisionError �߻�
        raise NegativeDivisionError(b)
    return a/b


try:
    ret = PositiveDevide(10, -3)
    print('10 / 3 = {0}'.format(ret))
except NegativeDivisionError as e:     # ����� ���� ������ ���
    print('Error - Second argument of PositiveDevide is ', e.value)
except ZeroDivisionError as e:         # '0'���� ������ ���
    print('Error - ', e.args[0])
except :         # �� �� ��� ������ ���
    print(e.args)
