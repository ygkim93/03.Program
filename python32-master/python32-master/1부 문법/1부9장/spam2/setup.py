# -*- coding: cp949 -*-
# ���̽�
# ����� : 'setup.py install' ����� ��ġ�� ���ÿ� ����˴ϴ�. 
# 'setup.py --help'ó�� �����Ͻø� �ڼ��� ������� �� �� �ֽ��ϴ�.
from distutils.core import setup, Extension
spam_mod = Extension('spam', sources = ['spammodule.c'])
setup(name = "spam",
    version = "1.0",
    description = "A sample extension module",
    ext_modules = [spam_mod],
)
