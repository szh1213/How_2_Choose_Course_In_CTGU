import os
os.chdir('C:/Users/szh1213/Desktop/python/爬虫练习/data/未识别/')
txt = []
pic = os.listdir()
if len(pic)<2:
    exit()
for i in range(len(pic)):
    txt.append(pic[i])
for i in range(len(txt)):
    os.rename(txt[i],str(i)+'_'+str(i)+'.jpg')
for i in range(len(txt)):
    os.rename(str(i)+'_'+str(i)+'.jpg',str(i)+'.jpg')
print('ok')
