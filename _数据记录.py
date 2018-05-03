from PIL import Image
import os
path = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/data/'
mylib = 'C:/Users/szh1213/Desktop/python/爬虫练习/mylib/'
pp = [-100,5,17,29,41]
name = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D',\
             'E','F','G','H','i','J','K','M','N','P','Q','R','S','T',\
             'U','W','X','Y','Z']
image = Image.open(path+'0_0'+'.jpg')
imgry = image.convert('L')
for tname in range(33):
    os.chdir(mylib+name[tname]+'/')
    pic = os.listdir()
    index = 1
    print(tname,end=' ')
    for i in range(len(pic)):
        if pic[i][len(pic[i])-1]== 'g':
            imgry = Image.open(pic[i])
        fname = name[tname]+'_'+str(index)+'.txt'
        index += 1
        with open(pic[i][:len(pic[i])-3]+'txt',"w")as f:
            for j in range(10):
                for i in range(12):
                    if imgry.getpixel((i,j))<120:
                        f.write('1')
                    else:
                        f.write('0')
                f.write('\n')
print('ok')
mylib = 'C:/Users/szh1213/Desktop/python/爬虫练习/mylib/'
mytable = []
mylist = []
realtxt = []
for i in range(33):
    mytable.append([])
    mylist.append([])
    os.chdir(mylib+name[i]+'/')
    txt = os.listdir()
    realtxt.append([])
    for each in txt:
        if each[len(each)-1]=='t':
            realtxt[i].append(each)
    for index in range(len(realtxt[i])):
        mytable[i].append([])
        mylist[i].append([])
        with open(mylib+name[i]+'/'+realtxt[i][index],'r') as rf:
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
os.chdir(mylib)
'''with open('mybook.txt','w')as book:
    for i in range(33):
        for index in range(len(mytable[i])):
            book.write('tt')
            for j in range(22):
                if mylist[i][index][j]<10:
                    book.write('0'+str(mylist[i][index][j]))
                else:
                    book.write(str(mylist[i][index][j]))
        book.write('nn')'''
