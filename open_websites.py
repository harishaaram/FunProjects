#This Program will save all the pdf from the url to your local directory

import urllib, os
from BeautifulSoup import *

url = 'http://www.cs.iit.edu/~cs430/'
dir_path = "/home/harish/Desktop/test/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
soup.prettify()#html document with proper indentation

#initialization
tags = soup.findAll('a', href=True)
count = 0
saveas = []
already_exist = bool


#Checking in the local folder for the filename
def check_for_file(fname):
        for root, dirs, files in os.walk(dir_path):
            if fname in files:
                return True
        return False

#saving with the word after the last two(because two pdf with same name can exist in different path) backward slash
def write_to_folder(saveas_splited):
    if len(saveas_splited) > 1:
        save_filename = saveas_splited[len(saveas_splited) -2] +'_'+saveas_splited[len(saveas_splited) -1]
        already_exist = check_for_file(save_filename)
        if already_exist == False:
            urllib.urlretrieve(download_link,dir_path+save_filename)
    else:
        already_exist = check_for_file(saveas_splited[0])
        if already_exist == False:
            urllib.urlretrieve(download_link,dir_path+saveas_splited[0])
    return True

#looping through links
for link in tags:
    filename = link.get('href')
    download_link = url + filename

    if filename[len(filename)-3:] == 'pdf':
        saveas = filename
        saveas_splited = saveas.split('/')
        write_to_folder(saveas_splited)


