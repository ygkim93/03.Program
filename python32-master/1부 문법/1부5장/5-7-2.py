# -*- coding: cp949 -*-
class GString:
    def __init__(self, init = None):   
        self.content = init

    def __sub__(self, str):             # '-'������ �ߺ�
       print("- opreator is called!")

    def __isub__(self, str):            # '-='������ �ߺ�
        print("-= opreator is called!")

g = GString("aBcdef")
g - "a"     # ��� ���: - opreator is called!
g -= "a"    # ��� ���: -= opreator is called!
