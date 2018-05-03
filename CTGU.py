#-*-coding:utf-8-*-
import os,re,sys,requests,queue,xlrd
from time import sleep
from bs4 import BeautifulSoup
from lxml import etree
from PIL import Image
from hashlib import md5
from datetime import datetime
mylist=[]
name = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D',\
             'E','F','G','H','i','J','K','M','N','P','Q','R','S','T',\
             'U','W','X','Y','Z']
#userName=input('输入学号：')
#passWord=input('输入密码：')
userName='2016105405'
passWord='425451'
userKey=''
svip = md5(bytes('szh1213_20180101'.encode('utf-8')))
svip.update(userName[:].encode('utf-8'))
svipResult = svip.hexdigest()
vip = md5(bytes(str('szh1213_'+str(datetime.now().year)).encode('utf-8')))
vip.update(userName[:].encode('utf-8'))
vipResult = vip.hexdigest()
with open('密匙.txt','r')as mishi:
    userKey+=str(mishi.read())
'''if userKey != svipResult and userKey != vipResult:
    print('密匙无效')
    sleep(3)
    sys.exit()'''
theType=[]
theName=[]
theClass=[]
excel=xlrd.open_workbook('课程.xlsx').sheets()[0]
for i in range(1,excel.nrows):
    theType.append('000')
    theName.append(excel.cell(i,0).value)
    theClass.append(excel.cell(i,1).value)

with open('mybook.txt','r')as book:
    for i in range(33):
        mylist.append([])
        while True:
            if book.read(2)=='tt':
                mylist[i].append([])
                for j in range(22):
                    mylist[i][len(mylist[i])-1].append(int(book.read(2)))
            else:
                break
print('初始化完毕')
def collation(imgry,error):
    imgtable = []
    imglist = []
    for py in range(10):
        imgtable.append([])
        for px in range(12):
            if imgry.getpixel((px,py))<120:
                imgtable[py].append(1)
            else:
                imgtable[py].append(0)
    for y in range(10):
        imglist.append(sum(imgtable[y]))
    for x in range(12):
        tmpsum = 0
        for y in range(10):
            tmpsum += imgtable[y][x]
        imglist.append(tmpsum)
    for i in range(33):
        for index in range(len(mylist[i])):
            if mylist[i][index]==imglist:
                os.remove('tmperror.jpg')
                print(name[i],end='')
                return 0,name[i]
            elif i==32 and index==len(mylist[i])-1:
                os.rename('tmperror.jpg','error'+str(error+1)+'.jpg')
                print('?',end='')
                return 1,'?'
url = "http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1"
imgUrl = "http://210.42.38.26:84/jwc_glxt/ValidateCode.aspx"
Student_Score='http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx'
Course_Choice='http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx'
Course_Query='http://210.42.38.26:84/jwc_glxt/Course_Choice/Stu_Course_Query.aspx'
PlanToStudy_Query='http://210.42.38.26:84/jwc_glxt/Plan_To_Study/PlanToStudy_Query.aspx'
s = requests.session()
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0;'+\
        ' WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '+\
        'Chrome/63.0.3239.108 Safari/537.36'
}
def login(xuehao,mima):
    response = s.get(url)
    soup=BeautifulSoup(response.content,'lxml')
    t__VIEWSTATE=soup.find_all('input',id='__VIEWSTATE')
    t__EVENTVALIDATION=soup.find_all('input',id='__EVENTVALIDATION')
    viewstate=re.findall('value="(.*?)"',str(t__VIEWSTATE))[0]
    eventvalidation=re.findall('value="(.*?)"',str(t__EVENTVALIDATION))[0]
    image = s.get(imgUrl, stream=True).content
    try:
        with open("code.jpg" ,"wb") as jpg:
            jpg.write(image)
    except IOError:
        print("IO Error\n")
    finally:
        jpg.close
    tmpimage=Image.open('code.jpg')
    tmpimg = tmpimage.convert('L')
    code=''
    print('验证码自动识别结果：',end='')
    error=0
    for start in [5,17,29,41]:
        tmpimg.crop((start,6,start+12,16)).save('tmperror.jpg')
        pimg = Image.open('tmperror.jpg')
        code += collation(pimg,error)[1]
    print()
    if error:
        return error
    data = {
    '__VIEWSTATE':viewstate,
    '__EVENTVALIDATION':eventvalidation,
    'txtUserName':xuehao,
    'txtPassword':mima,
    'CheckCode':code,
    'btnLogin.x':'37',
    'btnLogin.y':'12'
    }
    last=s.post(url,data=data,headers=headers)
    soup=BeautifulSoup(last.content,'lxml')
    headid=re.findall('id="(.*?)"',str(soup.find('head')))[0]
    if headid=='ctl00_Head1':
        print('成功进入教务系统')
    else:
        print('学号或密码错误或重复登陆')
        sleep(3)
        sys.exit()
    return error

def myscore():
    szh=s.get(Student_Score)
    soup=BeautifulSoup(szh.content,'lxml')
    return soup.find_all('table',id="ctl00_MainContentPlaceHolder_GridScore")[0]
def myquery():
    szh=s.get(Course_Query)
    soup=BeautifulSoup(szh.content,'lxml')
    return soup.find_all('table',id="ctl00_MainContentPlaceHolder_GridCourse_Q")[0]
def myplan():
    szh=s.get(PlanToStudy_Query)
    soup=BeautifulSoup(szh.content,'lxml')
    table = soup.find_all('table',id="ctl00_MainContentPlaceHolder_GridScore")[0]
    for tr in table:
        if '未修习' in str(tr):
            for i in range(len(theName)):
                if list(tr)[2].get_text()==theName[i]:
                    theType[theName.index(theName[i])]=list(tr)[5].get_text()
def mychoice(courseName,courseClass):
    szh=s.get(Course_Choice)
    soup=BeautifulSoup(szh.content,'lxml')
    viewstate=re.findall('value="(.*?)"',str(soup.find_all('input',id='__VIEWSTATE')[0]))[0]
    eventvalidation=''
    try:
        eventvalidation+=re.findall('value="(.*?)"',str(soup.find_all('input',id='__EVENTVALIDATION')[0]))[0]
    except:
        return 1
    poption=soup.find_all('option')
    for i in range(len(list(poption))):
        courseTypeid=re.findall('value="(.*?)"',str(list(poption)[i]))[0]
        data = {
        '__VIEWSTATE':viewstate,
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__EVENTVALIDATION':eventvalidation,
        'ctl00$MainContentPlaceHolder$School_Year':'2018',
        'ctl00$MainContentPlaceHolder$School_Term':'1',
        'ctl00$MainContentPlaceHolder$BtnSearch.x':'6',
        'ctl00$MainContentPlaceHolder$BtnSearch.y':'6',
        'ctl00$MainContentPlaceHolder$Course_Type':courseTypeid
        }
        try:
            szh=s.post(Course_Choice,data=data,headers=headers)
            print('进入到'+list(poption)[i].get_text()+courseTypeid,end=' ')
            
            soup=BeautifulSoup(szh.content,'lxml')
            eventtarget,viewstate,eventargument,eventvalidation='','','',''
            try:
                eventtarget+=re.findall("\('(.*?)'",str(soup.find_all('a',text=courseName)[0]))[0]
                eventargument+=re.findall(",'(.*?)'",str(soup.find_all('a',text=courseName)[0]))[0]
                print('ddd')
                eventvalidation+=re.findall('value="(.*?)"',str(soup.find_all('input',id='__EVENTVALIDATION')[0]))[0]
                viewstate+=re.findall('value="(.*?)"',str(soup.find_all('input',id='__VIEWSTATE')[0]))[0]
                data = {
                '__VIEWSTATE':viewstate,
                '__EVENTTARGET':eventtarget,
                '__EVENTARGUMENT':eventargument,
                '__EVENTVALIDATION':eventvalidation,
                'ctl00$MainContentPlaceHolder$School_Year':'2018',
                'ctl00$MainContentPlaceHolder$School_Term':'1',
                'ctl00$MainContentPlaceHolder$Course_Type':courseTypeid
                }
                print('找到'+courseName)
                break
                szh=s.post(Course_Choice,data=data,headers=headers)
                soup=BeautifulSoup(szh.content,'lxml')
                table = soup.find_all('table',id="ctl00_MainContentPlaceHolder_GridCourse")[0]
                coursehref=''
                for tr in table:
                    for td in tr:
                        if courseClass in str(td):
                            coursehref=re.findall('href="(.*?)"',str(tr))[0]
                s.get('http://210.42.38.26:84/jwc_glxt/Course_Choice/'+coursehref)
                print(coursehref[len(coursehref)-6:len(coursehref)-1])
                gheaders={
                    'Referer':'Referer: http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0;'+\
                    ' WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '+\
                    'Chrome/63.0.3239.108 Safari/537.36'}
                s.get('http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choose_Type.aspx',headers=gheaders)
                szh=s.get('http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choose_Confirm.aspx',headers=gheaders)
                soup=BeautifulSoup(szh.content,'lxml')
                viewstate=re.findall('value="(.*?)"',str(soup.find_all('input',id='__VIEWSTATE')[0]))[0]
                eventvalidation=re.findall('value="(.*?)"',str(soup.find_all('input',id='__EVENTVALIDATION')[0]))[0]
                data = {
                '__VIEWSTATE':viewstate,
                '__EVENTVALIDATION':eventvalidation,
                'Buttonconfirm':'关闭本窗口'
                }
                gheaders['Referer']='http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choose_Confirm.aspx'
                s.post('http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choose_Confirm.aspx',data=data,headers=gheaders)
                print('成功选到'+courseName)
                return 0
            except:
                sys.stdout.flush()
                sys.stdout.write('\r进入到{} 没有{}'.format(list(poption)[i].get_text(),courseName))
                sys.stdout.flush()
        except:
            pass
    
while login(userName,passWord):
    print('发生了小概率的识别问题，再次识别中........')
myplan()
'''with open('选课结果.html','w') as free:
    free.write(str(myquery().encode('ascii')))
os.system('explorer 选课结果.html')'''
for j in range(len(theType)):
    while mychoice(theName[j],theClass[j]):
        for left in range(10):
            sys.stdout.write('\r选课系统未开放 {}s 后继续，若此时关掉程序则为未退出系统'.format(10-left))
            sys.stdout.flush()
            sleep(1)
    #print(theName[j]+theClass[j]+'不存在或超时')
    print()
'''with open('选课结果.html','w') as free:
    free.write(str(myquery().encode('ascii')))
os.system('explorer 选课结果.html')'''
s.get(url)
sleep(3)
