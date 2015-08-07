# -*- coding: cp949 -*-
import os, os.path, sys, time
os.environ['PATH'] = os.path.join(os.environ['JAVA_HOME'], r'jre\bin\client') + ';' + os.environ['PATH']
import lucene

BlogDir = "./data"
IndexDir = "./luceneIndex"
LutPath = IndexDir + "/lastupdatetime.txt"

class BlogSearcher(object):
	def __init__(self, blogDir, indexDir):
		"�ʱ�ȭ �۾�"
		lucene.initVM(lucene.CLASSPATH)		# JVM�� �ʱ�ȭ�մϴ�.
    
		self.blogDir = blogDir
		self.indexDir = indexDir
		self.analyzer = lucene.StandardAnalyzer()
		self.store = lucene.FSDirectory.getDirectory(self.indexDir)

	def __MakeResultFormat(self, hits, searcher):
		"�˻� ��� �ۼ�"
		ret = []
		for h in hits:
			doc = lucene.Hit.cast_(h).getDocument()
			ret.append((doc.get("bloger").encode("cp949"), doc.get("path").encode("cp949")))

		searcher.close()
		return tuple(ret)
	
	def SearchExactContents(self, keyword):
		"��α� ���뿡 ���ϼ� Exactch Matching ����"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		k = keyword.decode('cp949').encode('utf-8')
		query = lucene.QueryParser('contents', self.analyzer).parse(k)

		hits = searcher.search(query)
		print ("%s matching documents" % hits.length())

		return self.__MakeResultFormat(hits, searcher)

	def SearchPrefixContents(self, keyword):
		"��α� ���뿡 ���Ͽ� Prefix Matching ����"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		
		k = keyword.decode('cp949').encode('utf-8')
		query = lucene.PrefixQuery( lucene.Term("contents", k) )

		hits = searcher.search(query)
		print ("%s matching documents" % hits.length())	

		return self.__MakeResultFormat(hits, searcher)

	def SearchPrefixAll(self, keyword):
		"��α� ����� ID�� ���ؿ� Prefix Matching ����"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		keyword+="*"
		k = keyword.decode('cp949').encode('utf-8')

		tqBloger = lucene.WildcardQuery( lucene.Term("bloger", k) )
		tqContents = lucene.WildcardQuery( lucene.Term("contents", k) )

		qBoolean = lucene.BooleanQuery()
		qBoolean.add(tqBloger, lucene.BooleanClause.Occur.SHOULD)
		qBoolean.add(tqContents, lucene.BooleanClause.Occur.SHOULD)

		hits = searcher.search(qBoolean)
		print ("%s matching documents" % hits.length())

		return self.__MakeResultFormat(hits, searcher)

	def SearchExactAll(self, keyword):
		"��α� ����� ID�� ���ؿ� Exact Matching ����"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		k = keyword.decode('cp949').encode('utf-8')

		tqBloger = lucene.TermQuery(lucene.Term("bloger", k))
		tqContents = lucene.TermQuery(lucene.Term("contents", k))

		qBoolean = lucene.BooleanQuery()
		qBoolean.add(tqBloger, lucene.BooleanClause.Occur.SHOULD)
		qBoolean.add(tqContents, lucene.BooleanClause.Occur.SHOULD)

		hits = searcher.search(qBoolean)
		print ("%s matching documents" % hits.length())

		return self.__MakeResultFormat(hits, searcher)

	def UpdateIndex(self):
		"�ε����� �ֽ��� �������� ����"
		self.lastIndexingTime = self.__ReadLatestUpdateTime()	# ���������� �ε����� �ð�(None-�ε����� ���� ����)
		writer = lucene.IndexWriter(self.store, self.analyzer, lucene.IndexWriter.MaxFieldLength(1048576))

		for root, dirnames, filenames in os.walk(self.blogDir):
			for filename in filenames:
				if not filename.endswith('.txt'):	# txt ������ �ƴ� ��� �ε������� ����	
					continue	

				path = os.path.join(root, filename)
				if (self.lastIndexingTime != None and self.lastIndexingTime >= int(os.stat(path).st_mtime)):
					continue		# �̹� �ε����� �߰��� �������� ���

				print("Adding: %s" % filename)
				try:
					f = open(path)
					content = f.read()
					f.close()

					doc = lucene.Document()
					doc.add(lucene.Field(	"bloger", 
											path.rsplit("\\", 2)[1],		# ������ ����ִ� ���丮�� ��ΰŷ� ����
											lucene.Field.Store.YES,
											lucene.Field.Index.UN_TOKENIZED))
					doc.add(lucene.Field(	"path", 
											path,
											lucene.Field.Store.YES,
											lucene.Field.Index.UN_TOKENIZED))
					doc.add(lucene.Field(	"contents", 
											content,
											lucene.Field.Store.NO,
											lucene.Field.Index.TOKENIZED))
					writer.addDocument(doc)
				except Exception, e:
					print("Failed in adding index: %s" % e)

		writer.optimize()
		writer.close()

		self.__WriteLatestUpdateTime()		# �ε����� �ð��� ���
		print("Completely updated!")
	
	def __WriteLatestUpdateTime(self):
		"�ε����� �ð��� ���"
		try:
			f = open(LutPath, "w")
			f.write(str(int(time.time())))		# ���� �ð��� ���
			f.close()
		except:
			print("Fail to WriteLatestUpdateTime")
			return False
		else:
			return True
	
	def __ReadLatestUpdateTime(self):
		"���� �ֱٿ� �ε����� �ð��� ����"
		try:
			f = open(LutPath, "r")
			t = int(f.read())
			f.close()
		except:
			return None					# �ε����� ó�� ����� ���
		else:
			return t


##################################################################################################

#if __name__ == '__main__':
# 	bs = BlogSearcher(BlogDir, IndexDir)

