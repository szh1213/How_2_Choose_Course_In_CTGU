from PIL import Image
#验证码存储位置
path = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/data/'
#验证码切割后存储位置
indexpath = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/indexdata/'
#四个字符起始像素点
pp = [-100,5,17,29,41]
for j in range(20):
    for i in range(10):
        image = Image.open(path+str(j)+'_'+str(i)+'.jpg')
        img = image.convert('L')
        for x in range(1,5):
            #验证码单个字符在原图中的位置
            child_img = img.crop((pp[x],6,pp[x]+12,16))
            #存下单个字符
            child_img.save(indexpath+str(x)+'/'+str(j)+'_'+str(i)+'_'+str(x)+'.jpg')
