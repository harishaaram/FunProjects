#This Program will save all the pdf from the url to your local directory

import urllib, re
from BeautifulSoup import *

url = 'http://www.cs.iit.edu/~cs430/'
dir_path = "/home/harish/Desktop/test/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
soup.prettify()#html document with proper indentation

tags = soup.findAll('a', href=True)
count = 0
saveas = []
for link in tags:
    filename = link.get('href')
    download_link = url + filename
    count = count+1
    if filename[len(filename)-3:] == 'pdf':
        saveas = filename
        print filename
        #saving with the word after the last backward slash
        if len(saveas.split('/')) > 1:
            urllib.urlretrieve(download_link,dir_path+saveas.split('/')[len(saveas.split('/')) -1])
        else:
            urllib.urlretrieve(download_link,dir_path+saveas.split('/')[0])
