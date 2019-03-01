import requests
from bs4 import BeautifulSoup


#print(requests.get('https://popculture.com/reality-tv/2018/12/06/bachelor-2019-cast-colton-underwood-leading-ladies/#17').text)
b = requests.get('https://popculture.com/reality-tv/2018/12/06/bachelor-2019-cast-colton-underwood-leading-ladies/#17').text
html = BeautifulSoup(requests.get('https://popculture.com/reality-tv/2018/12/06/bachelor-2019-cast-colton-underwood-leading-ladies/#17').text, 'lxml')
f = b.find("slideshow__title")  # find the first paragraph
#str(html.find("Colton Underwood's dramatic season"))  # the first paragraph, as a string. Includes embedded <b> etc.
print(f)

print(b[89135:])
###--------------------------------------------------------------------------------------------------------------------------------------------------------
'using twitter to get bachelor info'

l
