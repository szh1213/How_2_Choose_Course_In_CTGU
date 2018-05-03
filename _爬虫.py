import urllib.request
from PIL import Image
import os
#验证码地址
url = "http://210.42.38.26:84/jwc_glxt/ValidateCode.aspx"
#将抓到的验证码存在这里
path = 'C:/Users/szh1213/Documents/Processing/learnNumber_pde/data/'
print('正在从教务系统抓验证码............')
for i in range(41,100):
    for j in range(100):
        response = urllib.request.urlopen(url)
        img = response.read()
        with open(path+str(i)+'_'+str(j)+'.jpg','wb') as f:
            f.write(img)
        print(i,j)
