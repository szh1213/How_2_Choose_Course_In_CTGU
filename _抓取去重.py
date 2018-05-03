from PIL import Image
import os
os.chdir('C:/Users/szh1213/Desktop/python/爬虫练习/data/未识别/')
pic = os.listdir()
imgtable = []
movepic = []
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
for i in range(len(pic)-1):
    for j in range(i+1,len(pic)):
        if imgtable[i]==imgtable[j]:
            movepic.append(pic[i])
            break
for i in range(len(movepic)):
    os.remove(movepic[i])
print('ok')
