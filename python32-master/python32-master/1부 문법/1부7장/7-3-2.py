# -*- coding: cp949 -*-
def devide(a, b):
    return a/b

try:
    c = devide(5, 'apple')
except Exception:
    print('��~ ���� �������� �𸣰ھ��!!')  # ��� ������ ���Ͽ� �� �κп��� ó�� 
except ZeroDivisionError:
    print('�ι�° ���ڴ� 0�̸� �ȵ˴ϴ�.')
except TypeError:
    print('��� �μ��� �����̿��� �մϴ�.')
