# -*- coding: cp949 -*-
class MyClass:
    def __init__(self, value):  # ������ �޼ҵ�
        self.Value = value
        print("Class is created! Value = ", value)
        
    def __del__(self):          # �Ҹ��� �޼ҵ�
        print("Class is deleted!")

def foo():  
    d = MyClass(10)      # �Լ� foo ��Ͼȿ����� �ν��Ͻ� ��ü d�� ����

foo() 
