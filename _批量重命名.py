import os
mylib = 'C:/Users/szh1213/Desktop/python/爬虫练习/mylib/'
name = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D',\
             'E','F','G','H','i','J','K','M','N','P','Q','R','S','T',\
             'U','W','X','Y','Z']
txt = []
for tname in range(33):
    txt.append([])
    os.chdir(mylib+name[tname]+'/')
    pic = os.listdir()
    for i in range(len(pic)):
        if pic[i][len(pic[i])-1]== 'g':
            txt[tname].append(pic[i])
        elif pic[i][len(pic[i])-1]== 't':
            os.remove(pic[i])
for tname in range(33):
    os.chdir(mylib+name[tname]+'/')
    for i in range(len(txt[tname])):
        os.rename(txt[tname][i],name[tname]+'tpo_'+str(i)+'.jpg')
    for i in range(len(txt[tname])):
        os.rename(name[tname]+'tpo_'+str(i)+'.jpg',name[tname]+'_'+str(i)+'.jpg')
print('ok')
