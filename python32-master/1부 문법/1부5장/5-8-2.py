# -*- coding: cp949 -*-
class Person:
    " �θ� Ŭ���� "
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber

    def PrintInfo(self):    
        print ("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

    def PrintPersonData(self):
        print ("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Student(Person):
    " �ڽ� Ŭ���� "
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)    # ��������� Person �����ڸ� ȣ��
        self.Subject = subject
        self.StudentID = studentID
