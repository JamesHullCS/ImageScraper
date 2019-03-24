from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://twitter.com/NBA2K_MyTEAM') #grabs all the images from this URL
bs = BeautifulSoup(html, 'html.parser') #takes html data from the url provided
images = bs.find_all('img', {'src':re.compile('.jpg')}) #Finds all images in jpg format

file= open("Links.txt","w+") #Creates a .txt that has write permissions

for image in images: #says for each link out of links
    file.write(image['src']+'\n') #Write to the resquested



