from PIL import Image
path = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/data/'
indexpath = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/indexdata/'
pp = [-100,5,17,29,41]
for j in range(20):
    for i in range(10):
        image = Image.open(path+str(j)+'_'+str(i)+'.jpg')
        img = image.convert('L')
        for x in range(1,5):
            child_img = img.crop((pp[x],6,pp[x]+12,16))
            child_img.save(indexpath+str(x)+'/'+str(j)+'_'+str(i)+'_'+str(x)+'.jpg')
