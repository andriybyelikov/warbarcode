from bs4 import BeautifulSoup as bs
import urllib
import re

index_html = urllib.request.urlopen("https://en.wikipedia.org/wiki/Timeline_of_wars")
index_soup = bs(index_html, features="html5lib")
for period_url in index_soup.ul.find_all('a'):
    period_html = urllib.request.urlopen("https://en.wikipedia.org" + period_url['href'])
    period_soup = bs(period_html, features="html5lib")
    for tbody in period_soup.find_all('tbody'):
        for tr in tbody.find_all('tr'):
            elems = tr.find_all('td')
            if len(elems) >= 2:
                begin = elems[0].contents[0]
                end = elems[1].contents[0]
                if isinstance(begin, str) and isinstance(end, str):
                    begin_bc = begin.find('BC') != -1
                    end_bc = end.find('BC') != -1
                    begin_year = re.search('\d+', begin)
                    end_year = re.search('\d+', end)
                    if begin_year != None and end_year != None:
                        begin = ("-" if begin_bc else "") + begin_year.group(0)
                        end = ("-" if end_bc else "") + end_year.group(0)
                        print(begin + "," + end)
