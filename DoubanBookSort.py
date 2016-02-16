#!/bin/python2.7
# -*- coding:utf-8 -*-

import re
import urllib

class book:
    title = ""
    author = ""
    url = ""
    img = ""
    rate = 0.0

    def __init__(self, Title, Author, Url, Img, Rate):
        self.title = Title
        self.author = Author
        self.url = Url
        self.img = Img
        self.rate = Rate

    def content(self):
        return "Title:%s\tAuthor:%s\tUrl:%s\tImg:%s\tRate:%s\n"\
              %(self.title,self.author,self.url,self.img,self.rate)

def finder(page, pat):
    content = re.search(pat,page)
    if not content:
        print "Failed in url"
        exit(1)
    return content.group()

def makeHtml(blist,path):
    fp = open(path,'w+')
    Start = '''<!DOCTYPE html>
<html lang="zh-cmn-Hans" class=" book-new-nav">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>豆瓣图书Top250排序 | Alanzjl</title>

<script>!function(f){var h=function(o,n,m){var k=new Date(),j,l;n=n||30;m=m||"/";k.setTime(k.getTime()+(n*24*60*60*1000));j="; expires="+k.toGMTString();for(l in o){f.cookie=l+"="+o[l]+j+"; path="+m}},d=function(m){var l=m+"=",o,n,j,k=f.cookie.split(";");for(n=0,j=k.length;n<j;n++){o=k[n].replace(/^\s+|\s+$/g,"");if(o.indexOf(l)==0){return o.substring(l.length,o.length).replace(/\"/g,"")}}return null},e=f.write,b={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},a=function(l,k){var j=new Image();j.onload=function(){};j.src="http://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(l)+"&environment="+encodeURIComponent(k)},i=function(k){try{e.call(f,k)}catch(j){e(k)}},c=/<script.*?src\=["']?([^"'\s>]+)/ig,g=/http:\/\/(.+?)\.([^\/]+).+/i;f.writeln=f.write=function(k){var j=c.exec(k),l;if(!j){i(k);return}l=g.exec(j[1]);if(!l){i(k);return}if(b[l[2]]){i(k);return}if(d("hj")==="tqs"){return}a(j[1],location.href);h({hj:"tqs"},1);setTimeout(function(){location.replace(location.href)},50)}}(document);</script>


  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">

  <script>var _head_start = new Date();</script>

  <link href="http://img3.douban.com/f/book/9378a88cec03259a21648c0c3b55eaa6fa577d45/css/book/master.css" rel="stylesheet" type="text/css">

  <style type="text/css"></style>
  <script src="http://img3.douban.com/f/book/e9d9543ebc06f2964039a2e94898f84ce77fc070/js/book/lib/jquery/jquery.js"></script>
  <script src="http://img3.douban.com/f/book/36c6bb0e275c61fbb7b3294e6bccb7a2ba992522/js/book/master.js"></script>



  <script>  </script>
  <link rel="stylesheet" href="http://img3.douban.com/misc/mixed_static/752a6657ef371706.css">

</head>
<body>

    <script>var _body_start = new Date();</script>


	<div id="db-nav-book" class="nav">
  		<div class="nav-wrap">
    		<div class="nav-primary">
    			<div class="nav-logo">
        			<a href="http://alanzjl.com">豆瓣读书</a>
    			</div>
			</div>
    	</div>
  	</div>


	 <div id="wrapper">


  <div id="content">

    <h1>豆瓣读书Top250逆序 | Alanzjl</h1>

    <div class="grid-16-8 clearfix">

      <div class="article">
  <div class="indent">



    <p class="ulfirst"></p>
'''
    End = '''<div id="footer">

<span id="icp" class="fleft gray-link">
&copy; 2015-2016 www.alanzjl.com Contact with me at alanzhaojl@gmail.com
</span>

  </div>
</body>
</html>
'''
    fp.write(Start)
    count = 1;
    for i in blist:
        url = i.url
        title = i.title
        img = i.img
        author = i.author
        rate = i.rate
        content = '''<table width=%"100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="'''+'%s'%url+'''"
              onclick="moreurl(this,{i:'0'})"
              >
              <img src="'''+'%s'%img+'''" width="64" />
            </a>
          </td>
          <td valign="top">
            <div class="pl2">
              <a href="'''+'%s'%url+'''" onclick=&#34;moreurl(this,{i:&#39;0&#39;})&#34; title="'''+'%s'%title+'''">
                '''+'No.%s %s'%(count,title)+'''
              </a>
                <br/>
            </div>
              <p class="pl">'''+'%s'%author+'''</p>
              <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">'''+'%s'%rate+'''</span>
              </div>
          </td>
        </tr>
        </table>
        <p class='ul'></p>
        '''
        fp.write(content)
        fp.write('\n\n\n')
        count+=1
    fp.write(End)


def run():
    count = 0
    run_times = 0;
    while count < 250:
        url = 'http://book.douban.com/top250?start=%d'%count
        page = urllib.urlopen(url).read()

        titlePat = re.compile(r'(?<=&#34; title=").*?(?=")')
        authorPat = re.compile(r'(?<=<p class="pl">).*?(?=/)')
        urlPat = re.compile(r'(?<=<a href=").*?(?=" onclick=&#34)')
        imgPat = re.compile(r'(?<=<img src=").*?(?=" width="64" />)')
        ratePat = re.compile(r'(?<="rating_nums">).*?(?=<)')

        title = finder(page, titlePat)
        author = finder(page, authorPat)
        url = finder(page, urlPat)
        img = finder(page, imgPat)
        rate = finder(page, ratePat)

        #print "%s %s %s %s %s\n"%(len(title),len(author),len(url),len(img),len(rate))
        newBook = book(title, author, url, img, rate)
        bookList.append(newBook)
        print "%s: "%count
        print newBook.content(),

        count += 1

bookList = []
run()
bookListSorted = sorted(bookList, key=lambda ele:ele.rate, reverse=1)

makeHtml(bookListSorted,'DoubanBook.html');

fp = open('123','w+')
count = 1
for i in bookListSorted:
    fp.write("%s: "%count)
    fp.write(i.content())
    count+=1
#print rateList


