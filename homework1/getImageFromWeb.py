import requests
import re
import json
# download image from the web
def download_img(url_info):
    if url_info[1]:
        print("-----------downloading image %s"%(url_info[0]))
        try:
            url = url_info[0]
            response = requests.get(url)
            img = response.content
            # Save Path
            path='%s' % (url_info[1])
            with open(path, 'wb') as f:
                f.write(img)
            return (True, path)
        except Exception as ex:
            print("--------Error----")
            pass
# get image url list
def getImg(url):
    r = requests.get(url)
    html = r.text.encode(r.encoding).decode()
    reg = 'src="(.+?\.jpg)" alt='# Regularization
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 1
    for imgurl in imglist:
        download_img([imgurl, "%s.jpg" % x])
        x+=1
'''
getImg("http://pic.yxdown.com/list/0_459_1.html")
url=[input(),input()]
download_img(url)
download_img(['http://i-4-yxdown.715083.com/2019/6/12/edbd74bb-6c58-47a4-9d90-9609de395f67.jpg?imageView2/2/q/65/w/192','pic.png'])
'''