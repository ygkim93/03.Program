# -*- coding: cp949 -*-
import sqlite3
import sys
import re

# �����ͺ��̽� ��� ���� 
if len(sys.argv) == 2:
	path = sys.argv[1]
else:
	path = ":memory:"

con = sqlite3.connect(path)
con.isolation_level = None	# Ʈ����Ǿ��� �ڵ� Ŀ���� �ǵ��� ����
cur = con.cursor()

buffer = ""			# ���� ���� 

def PrintIntro():
	"���α׷� ��Ʈ�� �޼���"
	print("pysqlite�� command ���α׷��Դϴ�.")
	print("Ư�� ��ɾ �˰� �����ø� '.help;'�� �Է��ϼ���.")
	print("SQL ������ ';'���� ������ �մϴ�.")

def PrintHelp():
	"����"
	print(".dump\t\t�����ͺ��̽��� ������ �����մϴ�.")

def SQLDump(con, file=None):
	"�����ͺ��̽� ���� ����"
	if file != None:
		f = open(file, "w")
	else:
		f = sys.stdout

	for l in con.iterdump():
		f.write("{0}\n".format(l))

	if f != sys.stdout:
		f.close()

PrintIntro()		# ��Ʈ�� �޼��� ���

while True:
	line = input("pysqlite>> ")		# ��ɾ� �Է�
	if buffer == "" and line == "":
		break;
	buffer += line
	
	if sqlite3.complete_statement(buffer):		# ';'���� ������ �������� �˻�
		buffer = buffer.strip()

		if buffer[0]==".":		# Ư�� ��ɾ��� ���
			cmd = re.sub('[ ;]', ' ', buffer).split()
			if cmd[0] == '.help':
				PrintHelp()
			elif cmd[0] == '.dump':
				if len(cmd) == 2:
					SQLDump(con, cmd[1])
				else:
					SQLDump(con)
		else:					# �Ϲ� SQL ������ ���
			try:
				buffer = buffer.strip()
				cur.execute(buffer)

				if buffer.lstrip().upper().startswith("SELECT"):	# SELECT ������ ���
					print(cur.fetchall())
			except sqlite3.Error as e:
				print("Error: ", e.args[0])
			else:
				print("������ ���������� ����Ǿ����ϴ�.") 
		buffer=""		# �Է� ���� �ʱ�ȭ
con.close()
print("���α׷��� �����մϴ�. �߿�~")
