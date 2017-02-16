#This Program will save all the pdf from the url to your local directory

import urllib, os
from BeautifulSoup import *

url = 'http://www.cs.iit.edu/~cs430/'
dir_path = "/home/harish/Desktop/test/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
soup.prettify()#html document with proper indentation

tags = soup.findAll('a', href=True)
count = 0
saveas = []
already_exist = bool


#Checking in the local folder for the filename
def check_for_file(fname, path):
        for root, dirs, files in os.walk(path):
            if fname in files:
                return True
        return False


for link in tags:
    filename = link.get('href')
    download_link = url + filename

    if filename[len(filename)-3:] == 'pdf':
        saveas = filename
        saveas_splited = saveas.split('/')

        #saving with the word after the last backward slash
        if len(saveas_splited) > 1:
            already_exist = check_for_file(saveas_splited[len(saveas_splited) -1],dir_path)
            if already_exist == False:
                urllib.urlretrieve(download_link,dir_path+saveas_splited[len(saveas_splited) -1])
        else:
            already_exist = check_for_file(saveas_splited[0],dir_path)
            if already_exist == False:
                urllib.urlretrieve(download_link,dir_path+saveas_splited[0])
