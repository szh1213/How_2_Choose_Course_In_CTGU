import os
mylib = 'C:/Users/szh1213/Desktop/python/爬虫练习/mylib/'
name = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D',\
             'E','F','G','H','i','J','K','M','N','P','Q','R','S','T',\
             'U','W','X','Y','Z']
txt = []
movetxt = []
for tname in range(33):
    txt.append([])
    os.chdir(mylib+name[tname]+'/')
    pic = os.listdir()
    txtf = []
    for i in range(len(pic)):
        if pic[i][len(pic[i])-1]== 't':
            txt[tname].append(pic[i])
    
    for i in range(len(txt[tname])):
        with open(txt[tname][i],'r') as fi:
            txtf.append(fi.read())

    for i in range(len(txtf)-1):
        for j in range(i+1,len(txtf)):
            if txtf[i]==txtf[j]:
                movetxt.append(mylib+name[tname]+'/'+txt[tname][i])
                print(txt[tname][i]+'    \t'+txt[tname][j])
                break
for i in range(len(movetxt)):
    os.remove(movetxt[i])
    os.remove(movetxt[i][:len(movetxt[i])-3]+'jpg')
print('ok')
