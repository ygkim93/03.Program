# -*- coding: cp949 -*-
def devide(a, b):
    return a/b

try:
    c = devide(5, 2)
except ZeroDivisionError:
    print('�ι�° ���ڴ� 0�̸� �ȵ˴ϴ�.')
except TypeError:
    print('��� �μ��� �����̿��� �մϴ�.')
except:
    print('ZeroDivisionError, TypeError�� ������ �ٸ� ����')
else:      # ���ܰ� �߻����� �ʴ� ���
    print('Result: {0}'.format(c))
finally:   # ���� �߻� ������ ������� ���� 
    print('�׻� finally ����� ����˴ϴ�.')
