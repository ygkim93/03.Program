# -*- coding: cp949 -*-
import weakref
class ObjectManager:
    def __init__(self):
        self.weakDict = weakref.WeakValueDictionary()

    def InputObject(self, obj):
        objectID = id(obj)                # �Է¹��� ��ü�� ID ����
        self.weakDict[objectID] = obj     # ���� ��ųʸ��� ������ �Է� 
        return objectID

    def GetObject(self, objectID):
        try:
            return self.weakDict[objectID]    # ��ü�� �����ϴ� ��� ��ȯ
        except:
            return None                       # ��ü�� �Ҹ�� ��� None ��ȯ
