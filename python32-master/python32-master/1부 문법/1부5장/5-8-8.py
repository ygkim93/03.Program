# -*- coding: cp949 -*-
class Animal:
    def __init__(self):
        print("Animal __init__()")

class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self)		# Animal ������ �޼ҵ� ȣ��
        print("Tiger __init__()")

class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)		# Animal ������ �޼ҵ� ȣ��
        print("Lion __init__()")

class Liger(Tiger, Lion):
    def __init__(self):
        Tiger.__init__(self)		# Tiger ������ �޼ҵ� ȣ��
        Lion.__init__(self)			# Lion ������ �޼ҵ� ȣ��
        print("Liger __init__()")
