import os
i=1
s1=''
s2=''
s3=''
c1='class="tm-article-snippet__title-link"><span>'
c2='</span></a></h2> <div '
c3='<div class="article-formatted-body article-formatted-body article-formatted-body_version-2"><p>'
c4='class="tm-article-snippet__title tm-article-snippet__title_h2"><a href="'
c5='<a href="'
c6='" data-article-link="" data-test-id="article-snippet\n'
res='Предаврительный просмотр. Нажмите q для выхода.\n--------------------------------------------------\n'
j1=input('Введите глубину поиска. Целое число не меньше 2 [50]: ')
if j1=='':
   j=50
else:
   j=int(j1)
   if j<2:
      j=2
j=j+1
while i<j:
     if i==1:
         w='proxychains wget https://habr.com/ru/all/ -O habr.html'

     else:
         w='proxychains wget https://habr.com/ru/all/page'+str(i)+'/ -O habr.html'
     os.system(w)
     f=open('habr.html')
     i=i+1
     for line in f:
         if c1 in line:
            a=line.find(c1)
            b=line.find(c2)
            d=line.find(c4)
            s1=(line[a+45:b:1])
            s2=(line[d+72:d+140:1])
            s2='https://habr.com'+s2
            e=s2.rfind('/')
            s2=s2[0:e:1]
            res=res+s1+' | ' +s2+'\n'
f.close()
#print(res)
f=open('result.txt','w')
f.write(res)
f.close()

