# -*- coding: cp949 -*-
class GString:
    def __init__(self, init = None):    # ������ 
        self.content = init

    def __sub__(self, str):             # '-' ������ �ߺ� 
        for i in str:
            self.content = self.content.replace(i, '')
        return GString(self.content)

    def Remove(self, str):              # Remove �޼ҵ�� '-' ������ �ߺ��� �����ϱ⿡ '__sub__'�� ��ȣ��
        return self.__sub__(str)
