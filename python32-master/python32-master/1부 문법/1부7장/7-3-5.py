# -*- coding: cp949 -*-
def devide(a, b):
    return a/b
try:
    c = devide(5, 0)
except (ZeroDivisionError, OverflowError, FloatingPointError): # ��õ� ������ ��� ó�� 
    print('��ġ ���� ���� �����Դϴ�.')
except TypeError:
    print('��� �μ��� �����̾�� �մϴ�.')
except Exception:
    print('��~ ���� �������� �𸣰ھ��!!')
