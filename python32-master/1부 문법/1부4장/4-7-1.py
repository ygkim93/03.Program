# -*- coding: cp949 -*-
import time
l = range(1000)

t = time.mktime(time.localtime())      # for������ �� ���ڸ� ����ϴ� ���
for i in l:
    print (i,)
t1 = time.mktime(time.localtime()) - t

t = time.mktime(time.localtime())      # join() �޼ҵ带 �̿��Ͽ� ����ϴ� ���
print (", ".join(str(i) for i in l))
t2 = time.mktime(time.localtime()) - t

print ("for ������ �� ���ڸ� ���")          # ������ �ð� ��� 
print ("Take {0} seconds".format(t1))
print ("join() �޼ҵ�� ���")
print ("Take {0} seconds".format(t2))
