# -*- coding: cp949 -*-
class Animal:
    def __init__(self):
        print("Animal __init__()")

class Tiger(Animal):
    def __init__(self):
        super().__init__()			# �θ� Ŭ������ ������ �޼ҵ� ȣ��
        print("Tiger __init__()")

class Lion(Animal):
    def __init__(self):
        super().__init__()			# �θ� Ŭ������ ������ �޼ҵ� ȣ��
        print("Lion __init__()")

class Liger(Tiger, Lion):
    def __init__(self):
        super().__init__()			# �θ� Ŭ������ ������ �޼ҵ� ȣ��
        print("Liger __init__()")
