# -*- coding: cp949 -*-
def foo(x):
	assert type(x) == int, "Input value must be integer"   # ���� ������ type�� ���������� �˻�
	return x*10

ret = foo("a")   # AssertionError�� �߻� 
print(ret)
