# -*- coding: cp949 -*-
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
    if i > 5:                       # i�� 5���� ū ���, ��ȸ ���� ������ break���� ����˴ϴ�.
        break
    print("Item: {0}".format(i))
else:
    print("Exit without break.")    # break�� ������ ����Ǳ� ������, ��µ��� �ʽ��ϴ�.
print("Always this is printed")
