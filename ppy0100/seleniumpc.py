from selenium import webdriver
from time import sleep
import re
import math
from time import  sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import threading
import pymysql
import  collections
#无界面
'''chrom_option=Options()
chrom_option.add_argument('headless')
bro=webdriver.Chrome(chrome_options=chrom_option)'''
'''inputs=bro.find_element_by_id('kw')
inputs.send_keys('python')
inputs.send_keys(Keys.ENTER)'''
def get_all_url():
    sleep(10)
    chrom_option = Options()
    chrom_option.add_argument('headless')
    bro = webdriver.Chrome(chrome_options=chrom_option)
    #bro=webdriver.Chrome()
    bro.get("https://www.dy2018.com/")
    windows=bro.window_handles#设置窗口句柄
    #bro.switch_to.window(windows[1])#选择当选窗口
    #bro.close()
    bro.switch_to.window(windows[0])
    lis=[]
    count=0
    for link in bro.find_elements_by_xpath("//div[@class='contain']/ul/li/a[@href]"):
        a=link.get_attribute('href')
        if count<15:
            lis.append(a)
            count=count+1

    bro.quit()
    return lis
    #wait=WebDriverWait(bro,10)

    #wait.until(EC.presence_of_element_located((By.ID,'content_left')))
def get_all_daddr(page_url):#获取电影名字及次下载链接
    chrom_option = Options()
    chrom_option.add_argument('headless')
    bro = webdriver.Chrome(chrome_options=chrom_option)
    #bro = webdriver.Chrome()
    bro.get(page_url)
    sleep(1)
    #name_page=collections.OrderedDict()
    link_lis=[]
    name_page=[]
    next_page=''
    try:
        for link in bro.find_elements_by_xpath("//td[@height='26']/b/a[contains(@href,'.html')]"):
            fmname=link.get_attribute("title")
            fmlink=link.get_attribute("href")
            name_page.append(fmname)
            print(fmlink)
            link_lis.append(fmlink)
            #print("%s:%s"%(fmname,fmlink))
        link=bro.find_elements_by_xpath("//div[@class='x']/p/a[contains(text(),'下一页')]")
        next_page=link[0].get_attribute("href")
        print(next_page)
    except:
        next_page=False
        print("到尾页")
    bro.quit()
    print(link_lis)
    return name_page,link_lis,next_page


def get_one_lkname(lktp_url,list1,li_tm30lk,li_tm30nm,name_page):#电获取电影下载链接
    chrom_option = Options()
    chrom_option.add_argument('headless')
    bro = webdriver.Chrome(chrome_options=chrom_option)
    #bro=webdriver.Chrome()
    bro.get(lktp_url)
    bro.implicitly_wait(10)
    wait=WebDriverWait(bro,10)
    wait.until(EC.presence_of_element_located((By.ID,'Zoom')))
    t=bro.page_source
    t1=BeautifulSoup(t,'lxml')
    t2=str(t1)
    bro.quit()
    try:

        res=re.findall(r'<a.*(thunder://\w+=?).*>.*</a>',t2)
        print("电影名：%s --链接：%s"%(name_page,res[0]))
        #list1.append(res[0])
        li_tm30lk.append(res[0])
        li_tm30nm.append(name_page)
    except:
        print("未获取")





def thred_run(list,li,name_page):
    li_tempnm=[]
    li_templk=[]

    for n in range(math.ceil(len(list)/5)):
        threds=[]
        for m in range(5):
            if (m+5*n) < len(list):
                t = threading.Thread(target=get_one_lkname, args=(list[m+5*n],li,li_templk,li_tempnm,name_page[m+5*n],))
                t.setDaemon(True)
                threds.append(t)
        for n1 in range(len(threds)):
            threds[n1].start()
        for n2 in range(len(threds)):
            threds[n2].join(20)

    return li_tempnm,li_templk

def Mysql_saves(flag,name,link):
    connect=pymysql.connect(host='localhost',user='root',port=3306,passwd='12345dfg',db='movie',charset='gbk')
    cursor=connect.cursor()
    table_name=['动作片','剧情片','爱情片','喜剧片','科幻片','恐怖片','动画片','惊悚片','战争片','犯罪片','国产剧','美剧','日韩剧','综艺','动漫']
    if flag==0:
        c_tabel="create table if not exists action_movie ( line_num int auto_increment primary key,mv_name char(200) , " \
                "link varchar(500))"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        print(len(name),len(link))
        ins_data="insert into action_movie (mv_name,link) values ('%s','%s')"
        try:
            for m in range(len(link)):#循环存数据

                cursor.execute(ins_data % (name[m], link[m]))
                connect.commit()

        except:
            print("asdsa")
        finally:
            connect.close()
    elif flag ==1:
        c_tabel = "create table if not exists story_movie (line_num int auto_increment primary key,mv_name char(100) , " \
                  " link varchar(500) )"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into story_movie (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag ==2:
        c_tabel = "create table if not exists romantic_movie (line_num int auto_increment primary key ,mv_name char(100) ," \
                  "link varchar(500) )"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into romantic_movie (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 3:
        c_tabel = "create table if not exists comedy_movie (line_num int auto_increment primary key,mv_name char(100) , " \
                  "link varchar(500)) "
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into comedy_movie (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag ==4:
        c_tabel = "create table if not exists science_movie (line_num int auto_increment  primary key ,mv_name char(100)," \
                  "link varchar(500) )"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into science_movie (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag ==5:
        c_tabel = "create table if not exists horror_movie (line_num int auto_increment primary key,mv_name char(100) ," \
                  "  link varchar(500)) "
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into horror_movie  (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag ==6:
        c_tabel = "create table if not exists cartoon (line_num int auto_increment primary key, mv_name char(100) , " \
                  "link varchar(500))  "
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into cartoon(mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag ==7:
        c_tabel = "create table if not exists thriller_movie (line_num int auto_increment  primary key , mv_name char(100)," \
                  "link varchar(500))"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into thriller_movie (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 8:
        c_tabel = "create table if not exists war_movie (line_num int auto_increment  primary key ,mv_name char(100)," \
                  "link varchar(500) ) "
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into war_movie (mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 9:
        c_tabel = "create table if not exists crime_movie (line_num int auto_increment  primary key ,mv_name char(100)," \
                  "link varchar(500) )"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into crime_movie(mv_name,link) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 10:
        c_tabel = "create table if not exists 国产剧 (电影序列 int auto_increment  primary key ,电影名 char(100)," \
                  "电影下载链接 varchar(500) )"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into 国产剧 (电影名,电影下载链接) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 11:
        c_tabel = "create table if not exists 美剧 (电影序列 int auto_increment  primary key , 电影名 char(100)," \
                  "电影下载链接 varchar(500) )"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into 美剧 (电影名,电影下载链接) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 12:
        c_tabel = "create table if not exists 日韩剧 (电影序列 int auto_increment primary key  ,电影名 char(100)," \
                  "电影下载链接 varchar(500)) "
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into 日韩剧 (电影名,电影下载链接) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
            connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag == 13:
        c_tabel = "create table if not exists 综艺 (电影序列 int auto_increment  primary key, 电影名 char(100) , " \
                  "电影下载链接 varchar(500))"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into 综艺 (电影名,电影下载链接) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
                connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    elif flag ==14:
        c_tabel = "create table  if not exists 动漫 (电影序列 int auto_increment primary key ,电影名 char(100) , " \
                  "电影下载链接 varchar(500))"
        if cursor.execute(c_tabel):
            cursor.execute(c_tabel)
            connect.commit()
        ins_data = "insert into 动漫 (电影名,电影下载链接) values ('%s','%s')"
        try :
            for i in range(len(link)):#循环存数据
                cursor.execute(ins_data % (name[i], link[i]))
            connect.commit()
        except:
            print("无资源或重复")
        finally:
            connect.close()
    else:
        print("全部存完")


    return

if __name__ == "__main__":
    page_link_list=get_all_url()#第一层链接
    print(page_link_list)
    temp=()
    li=[]
    for i in range(len(page_link_list)):

        nm_pg = get_all_daddr(page_link_list[i])  # 第二层链接
        while 1:
            if nm_pg[2]:
                nm_lk=thred_run(nm_pg[1],li,nm_pg[0])
                print(nm_lk[0])
                Mysql_saves(flag=i,name=nm_lk[0],link=nm_lk[1])
                nm_pg=get_all_daddr(nm_pg[2])

            else:
                break













