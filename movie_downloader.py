import bs4
import codecs
import os
from urllib import urlopen



webpage = urlopen('https://www.sratim.co.il/top500imdb.php').read().decode('utf-8')
soup = bs4.BeautifulSoup(webpage, 'html.parser')
with codecs.open('movie_list.txt', 'w', 'utf-8') as f:
    for td in soup.findAll('td', {'class':'top500tab_secondbg_name'} ):
         f.writelines(td.find('a').text + os.linesep)
