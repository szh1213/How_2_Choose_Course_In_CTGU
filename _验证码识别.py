from PIL import Image
import os
path = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/data/'
where = 'C:/Users/szh1213/Desktop/python/爬虫练习/data/'
mylib = 'C:/Users/szh1213/Desktop/python/爬虫练习/mylib/'
mytable = []
mylist = []
name = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D',\
             'E','F','G','H','i','J','K','M','N','P','Q','R','S','T',\
             'U','W','X','Y','Z']
error = 0
for i in range(33):
    mytable.append([])         
    mylist.append([])
    os.chdir(mylib+name[i]+'/')
    txt = os.listdir()
    realtxt = []
    for each in txt:
        if each[len(each)-1]=='t':
            realtxt.append(each)
    for index in range(len(realtxt)):
        mytable[i].append([])
        mylist[i].append([])
        with open(mylib+name[i]+'/'+realtxt[index],'r') as rf:
            for y in range(10):
                mytable[i][index].append([])
                for x in range(12):
                    mytable[i][index][y].append(int(rf.read(1)))
                rf.read(1)
for i in range(33):
    for index in range(len(mytable[i])):
        for y in range(10):
            mylist[i][index].append(sum(mytable[i][index][y]))
        for x in range(12):
            tmpsum = 0
            for y in range(10):
                tmpsum += mytable[i][index][y][x]
            mylist[i][index].append(tmpsum)
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
        for index in range(len(mytable[i])):
            if mytable[i][index]==imgtable:
                os.remove(where+'未识别/tmperror.jpg')
                print(name[i],end='')
                return 0
            elif i==32 and index==len(mytable[i])-1:
                os.rename(where+'未识别/tmperror.jpg',\
                        where+'未识别/error'+str(error+1)+'.jpg')
                print('?',end='')
                return 1
for j in range(100):
    for i in range(100):
        image = Image.open(path+str(j)+'_'+str(i)+'.jpg')
        img = image.convert('L')
        for start in [5,17,29,41]:
            img.crop((start,6,start+12,16)).save(where+'未识别/tmperror.jpg')
            pimg = Image.open(where+'未识别/tmperror.jpg')
            error += collation(pimg,error)
        print(' ',end='')
    print()
print('error: '+str(error))
