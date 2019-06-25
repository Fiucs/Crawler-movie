import re
import string

with open('C:\\Users\\FKU\\Desktop\\Why Is Our Society Crazy About Celebrities.txt','r') as f:
    text=f.read()
text1=text.replace('\n',' ').replace('?','')
print(text1)
text2=re.findall(r'[A-Za-z]+\'?-?[A-Za-z]+',text1)
print(text2)
text3=re.findall('don\W?t',text1)
print(text3)
print("每个单词出现的次数：\n")
list=[]
for word in text2:
    if word not in list:
        list.append(word)
        ls=re.findall(word,text1)
        print("%s:%d"%(word,len(ls)))





#if __name__ =="__main":
