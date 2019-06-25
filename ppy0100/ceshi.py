from selenium import webdriver
from time import sleep
import re
from time import  sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import threading
import  collections
import pymysql
'''
bro=webdriver.Chrome()
bro.get("https://www.dy2018.com/i/97140.html")
bro.implicitly_wait(10)
a1=bro.page_source
bro.close()
print(a1)
t1 = BeautifulSoup(a1, 'lxml')
t2 = str(t1)
if re.findall(r'<a.*(thunder://\w+=).*>.*</a>',t2):
    res=re.findall(r'<a.*(thunder://\w+=).*>.*</a>',t2)
    name1=re.findall(r'<p>◎片　　名　(.*)</p>',t2)
    name2=re.findall(r'<p>◎译　　名　(.*)</p>',t2)
    name3=[name1[0]+'/'+name2[0]]
    print(res[0])
    print(name3[0])
else:
    res=re.findall(r'<a.*(thunder://\w+=?).*>.*</a>',t2)
    print(res[0])
'''
connect=pymysql.connect(host='localhost',user='root',port=3306,passwd='12345dfg',db='movie',charset='gbk')
cursor=connect.cursor()
c_tabel="create table if not exists action_movie1 (line_num int auto_increment primary key, mv_name char(200) , " \
                "link varchar(500))"
s2="影名：2018年美国7.5分动作片《蚁人2：黄蜂女现身》BD双语双字"
s1= "thunder://QUFmdHA6Ly9kOmRAYS5keWdvZGo4LmNvbToxMjMxMS9bJUU3JTk0JUI1JUU1JUJEJUIxJUU1JUE0JUE5JUU1JUEwJTgyd3d3LmR5MjAxOC5jb21dJUU4JTlBJTgxJUU0JUJBJUJBMiVFRiVCQyU5QSVFOSVCQiU4NCVFOCU5QyU4MiVFNSVBNSVCMyVFNyU4RSVCMCVFOCVCQSVBQkJEJUU1JTlCJUJEJUU4JThCJUIxJUU1JThGJThDJUU4JUFGJUFEJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3Lm1wNFpa"
str="insert into action_movie1 (mv_name,link) select '电影名：2018年国7.5分动作片《蚁人2：黄蜂女现身》BD双语双字','thunder://QUFmdHA6Ly9kOmRAYS5keWdvZGo4LmNvbToxMjMxMS9bJUU3JTk0JUI1JUU1JUJEJUIxJUU1JUE0JUE5JUU1JUEwJTgyd3d3LmR5MjAxOC5jb21dJUU4JTlBJTgxJUU0JUJBJUJBMiVFRiVCQyU5QSVFOSVCQiU4NCVFOCU5QyU4MiVFNSVBNSVCMyVFNyU4RSVCMCVFOCVCQSVBQkJEJUU1JTlCJUJEJUU4JThCJUIxJUU1JThGJThDJUU4JUFGJUFEJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3Lm1wNFpa'" \
    "from dual where not exists (select * from action_movie1 where mv_name='电影名：2018年美国7.5分动作片《蚁人2：黄蜂女现身》BD双语双字')"
str1="insert into action_movie1 (mv_name,link) select '%s','%s' " \
     " from dual where not exists (select * from action_movie1 where mv_name='%s') "
cursor.execute(c_tabel)
connect.commit()
#cursor.execute("insert into action_movie (mv_name,link) values ('电影名：2018年美国7.5分动作片《蚁人2：黄蜂女现身》BD双语双字','thunder://QUFmdHA6Ly9kOmRAYS5keWdvZGo4LmNvbToxMjMxMS9bJUU3JTk0JUI1JUU1JUJEJUIxJUU1JUE0JUE5JUU1JUEwJTgyd3d3LmR5MjAxOC5jb21dJUU4JTlBJTgxJUU0JUJBJUJBMiVFRiVCQyU5QSVFOSVCQiU4NCVFOCU5QyU4MiVFNSVBNSVCMyVFNyU4RSVCMCVFOCVCQSVBQkJEJUU1JTlCJUJEJUU4JThCJUIxJUU1JThGJThDJUU4JUFGJUFEJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3Lm1wNFpa')")
#connect.commit()
#cursor.execute("insert into action_movie (mv_name,link) values ('电影名：20美国7.5分动作片《蚁人2：黄蜂女现身》BD双语双字','thunder://QUFmdHA6Ly9kOmRAYS5keWdvZGo4LmNvbToxMjMxMS9bJUU3JTk0JUI1JUU1JUJEJUIxJUU1JUE0JUE5JUU1JUEwJTgyd3d3LmR5MjAxOC5jb21dJUU4JTlBJTgxJUU0JUJBJUJBMiVFRiVCQyU5QSVFOSVCQiU4NCVFOCU5QyU4MiVFNSVBNSVCMyVFNyU4RSVCMCVFOCVCQSVBQkJEJUU1JTlCJUJEJUU4JThCJUIxJUU1JThGJTh1JUFEJTk3Lm1wNFpa')")
#connect.commit()
try:
    cursor.execute(str)
    connect.commit()
except:
    print("error")
cursor.execute(str1%(s2,s1,s2))
connect.commit()
connect.close()
for i in range(3):
    print("数字：%d"%(i))
    i = 0
    while 1:

        print("hehiha")
        if i<5 :
            i=i+1
        else:
            break
if 1 :
    print("1")
n=''
if len(n)!=0:
    print("-1")