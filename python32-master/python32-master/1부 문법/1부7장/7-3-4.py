# -*- coding: cp949 -*-
def devide(a, b):
    return a/b
try:
    c = devide(5, "af")
except TypeError as e:	# ���޵Ǵ� ���� �ν��Ͻ� ��ü�� e�� �޾Ƽ� ���
    print('����: ', e.args[0])
except Exception:
	print('��~ ���� �������� �𸣰ھ��!!')
