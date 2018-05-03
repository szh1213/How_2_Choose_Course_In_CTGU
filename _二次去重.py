from PIL import Image
import os
os.chdir('C:/Users/szh1213/Desktop/python/爬虫练习/data/未识别/')
pic = os.listdir()
movepic = []
imgtable = []
for i in range(len(pic)):
    imgtable.append([])
    imgry = Image.open(pic[i])
    for py in range(10):
        imgtable[i].append([])
        for px in range(12):
            if imgry.getpixel((px,py))<120:
                imgtable[i][py].append(1)
            else:
                imgtable[i][py].append(0)
mylib = 'C:/Users/szh1213/Desktop/python/爬虫练习/mylib/'
mytable = []
realtxt = []
name = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D',\
             'E','F','G','H','i','J','K','M','N','P','Q','R','S','T',\
             'U','W','X','Y','Z']

for i in range(33):
    mytable.append([])
    os.chdir(mylib+name[i]+'/')
    txt = os.listdir()
    realtxt.append([])
    for each in txt:
        if each[len(each)-1]=='t':
            realtxt[i].append(each)
    for index in range(len(realtxt[i])):
        mytable[i].append([])
        with open(mylib+name[i]+'/'+realtxt[i][index],'r') as rf:
            for y in range(10):
                mytable[i][index].append([])
                for x in range(12):
                    mytable[i][index][y].append(int(rf.read(1)))
                rf.read(1)
for i in range(len(imgtable)):
    for tname in range(33):
        for index in range(len(mytable[tname])):
            if mytable[tname][index]==imgtable[i]:
                movepic.append(pic[i])
                print(pic[i]+'  '+realtxt[tname][index])
os.chdir('C:/Users/szh1213/Desktop/python/爬虫练习/data/未识别/')
for i in range(len(movepic)):
    os.remove(movepic[i])
print('ok')
