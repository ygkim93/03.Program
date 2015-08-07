# -*- coding: cp949 -*-
import os, os.path, sys
os.environ['PATH'] = os.path.join(os.environ['JAVA_HOME'], r'jre\bin\client') + ';' + os.environ['PATH']
import lucene
lucene.initVM(lucene.CLASSPATH)		# Initialize  JVM

def	IndexCreate(fileDir, indexDir):
	analyzer = lucene.StandardAnalyzer()	# ������� ����ϴ� ��ü ����
	store = lucene.FSDirectory.getDirectory(indexDir)
	writer = lucene.IndexWriter(store, analyzer)

	for root, dirnames, filenames in os.walk(fileDir):	# �Է¹��� �������� �ؽ�Ʈ ���ϸ� �˻�
		for filename in filenames:
			if not filename.endswith('.txt'):
				continue
			
			print("Adding: %s" % filename)
			try:
				path = os.path.join(root, filename)
				f = open(path)
				content = f.read()
				f.close()

				content = content.decode('cp949').encode('utf-8')	# ���ڵ��� 'utf-8'�� ����

				doc = lucene.Document()				# Document ��ü �߰�
				doc.add(lucene.Field(	"name", 	# ���ϸ�
										filename,
										lucene.Field.Store.YES,
										lucene.Field.Index.NO))
				doc.add(lucene.Field(	"path", 	# ���� ���
										path,
										lucene.Field.Store.YES,
										lucene.Field.Index.NO))
				if len(content) > 0:
					doc.add(lucene.Field(	"content", 		# ���� ����
											content,
											lucene.Field.Store.NO,
											lucene.Field.Index.TOKENIZED))
				else:
					print("Warning: No contents in %s" % filename)
				writer.addDocument(doc)				# �ε����� Document �߰�
			except Exception, e:
				print("Failed in adding index: %s" % e)

	writer.optimize()          # �ε��� ����ȭ �� IndexWriter ��ü �ݱ�
	writer.close()

def SearchKeyword(indexDir, keyword):
	directory = lucene.FSDirectory.getDirectory(indexDir)
	searcher = lucene.IndexSearcher(directory)		# �ε��� �˻� ��ü
	analyzer = lucene.StandardAnalyzer()

	print ("Searching for %s" % keyword)
	keyword = keyword.decode('cp949').encode('utf-8')
	queryParser = lucene.QueryParser('content', analyzer)				# ���� ����
	query = queryParser.parse(keyword)
	
	hits = searcher.search(query)					# �˻� ����
	print ("%s matching documents" % hits.length())	# ��� ����

	for h in hits:									# ��� ���
		doc = lucene.Hit.cast_(h).getDocument()
		print("Path: %s, name: %s" % (doc.get("path"), doc.get("name")))

	searcher.close()

if __name__ == '__main__':
	IndexCreate("./files", "./txt_index")
	SearchKeyword("./txt_index", "apple")
