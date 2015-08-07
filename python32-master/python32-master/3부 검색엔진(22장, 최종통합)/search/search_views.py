# -*- coding: cp949 -*-
from django.http import HttpResponse

#for template
from django.template import Context, loader

from BlogSearcher import *  # 3�� 2�忡�� �ߴ� BlogSearcher�� ����Ʈ �մϴ�.
import os

#global value
BlogDir = "./data" 
IndexDir = "./index"

listSize = 10
showLength = 100

Blog_prefixURL ="http://blog.daum.net/"

def ParameterInputError(req):
    html = "error"
    return HttpResponse(html)
    
def BlogSearchPage(req,mode,keyword,page=1): # req : request
    global listSize
    page = int(page)
    resultTup = callBlogSearch(mode,keyword)
    showItemTup = resultTup[((page-1)*listSize):(page*listSize)] # �����̽� 10���� ������ �����ɴϴ�.
    searchList = matchContentData(keyword,showItemTup) # �������� ǥ���� �����͸� �����մϴ�
    
    totalSize = len(resultTup)       # �˻� ��� �� �κп� �׺�����͸� ���� �κ��Դϴ�.
    pageCnt = totalSize / listSize
    if (totalSize % listSize ) != 0 :
	      pageCnt += 1
    
    pageList = range(1, pageCnt + 1)
    
    tpl = loader.get_template('search.html')   # ���ø� �ε�
    ctx = Context({ 
    		'searchList' : searchList,                   # ���������� ä�� �ݴϴ�.
    		'keyword' : keyword,
    		'mode': mode,
    		'pageList' : pageList,
    })
    
    html = tpl.render(ctx)
    return HttpResponse(html)
    
def callBlogSearch(mode,keyword):
    global BlogDir,IndexDir
    bs = BlogSearcher(BlogDir,IndexDir)
    if mode == "exAll":
        rfunc = bs.SearchExactAll
    elif mode == "preAll":
        rfunc = bs.SearchPrefixAll
    elif mode == "extCon":
        rfunc = bs.SearchExactContents
    elif mode == "preCon":
        rfunc = bs.SearchPrefixContents
    else:
        rfunc = bs.SearchExactAll
        
    searchTup = rfunc(keyword.encode('cp949'))
    return searchTup

def matchContentData(keyword,listTup):
    "���ø��� ���� �����͸� �����մϴ�."
    ResultData = []
    for item in listTup:
        conTitle,conPreview = makeContentPreview(keyword,item[1])
        conLink = makeContentLink(item[0],item[1])
        ResultData.append(({'preview':conPreview,'link':conLink,'title':conTitle}))
    return ResultData

def makeContentPreview(keyword,filepath):
    global showLength
    cFD = open(filepath)
    strTitle = cFD.readline()
    contData = cFD.read()
           
    #���� ���� ���ڿ� ���� ���ڸ� �����մϴ�.
    contData = contData.replace("&nbsp;","")        # &nbsp; �±׸� �����մϴ�.
    contData = contData.replace("\n","")              # ���θ��� ���ڸ� �����մϴ�.
    contData = contData.replace("\r","")              # �����ǵ� ���ڸ� �����մϴ�.
    contData = contData.strip()                       # ������ �����մϴ�.
     
    contData = contData.decode('utf-8')
    strTitle = strTitle.decode('utf-8')
    
    pos = contData.find(keyword)
    
    PreviewData = ""
    if pos > (showLength/2):
        PreviewData = contData[pos - (showLength / 2) : pos + (showLength / 2)]
    else:
        PreviewData = contData[0:showLength]
		
    if len(PreviewData) <= 0 :
        PreviewData = u"(������ ��� �ֽ��ϴ�)"
		
    # �����Ϳ��� Ű���忡 �ش� �ϴ� ���� ����ü�� ǥ���մϴ�.
    strTitle =  strTitle.replace(keyword, "<b>" + keyword + "</b>")
    PreviewData =  PreviewData.replace(keyword, "<b>" + keyword + "</b>")
        
    return strTitle,PreviewData

def makeContentLink(id,filepath):
    global Blog_prefixURL;
    list = filepath.split("\\")
    blog_uid = list[len(list)-1]
    blog_uid= blog_uid.replace(".txt","")
    return Blog_prefixURL + id + "/" + blog_uid



































