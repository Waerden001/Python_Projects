import requests
import bs4
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# Goggenheim 
page_1 = "https://archive.org/details/guggenheimmuseum?&sort=-downloads&page=1"
page_2 = "https://archive.org/details/guggenheimmuseum?&sort=-downloads&page=2"
page_3 = "https://archive.org/details/guggenheimmuseum?&sort=-downloads&page=3"
goggen_url = [page_1, page_2, page_3]

# Met, the time we write this script, met library has 49 pages of books 

base_link = "https://www.metmuseum.org/art/metpublications/titles-with-full-text-online?&searchtype=F&view=L&&rpp=12&pg="
met_url = []
for page_num in range(1, 50):
    link = base_link + str(page_num)
    met_url.append(link)
#TODO: download_page can be realized by the download_from_html function
download_page=[]
for page in met_url:
    res = requests.get(page)
    soup = bs4.BeautifulSoup(res.text)
    book_elem = soup.find_all(id="moreHyperLink")
    print(book_elem)
    for book in book_elem:
        new = book["href"]
        download_page.append("https://www.metmuseum.org"+new)

#TODO: construct the content list, this step can also be realized by the download_from_html function
content = []
for book in download_page:
    response = requests.get(book)
    soup= BeautifulSoup(response.text, "html.parser")     
    link = soup.find(id="m_download_pdf_link")
    if link != None:
      content.append(urljoin(book,link["href"]))
    else:
      print(book)
    #filename = os.path.join(folder_location,link["href"].split("/")[-1])
    #with open(filename,"wb") as f:
        #f.write(requests.get(urljoin(book,link["href"])).content)
        #print(urljoin(book,link["href"]))

# Metty

tail = ["%04d" % i for i in range(0,10000)]
content = []
head = "http://d2aohiyo3d3idm.cloudfront.net/publications/virtuallibrary/089236"
ext = ".pdf"
for num in tail:
    link = head + num + ext
    res = requests.get(link)
    if res.status_code == 200:
        content.append(link)
    if int(num)%100==0:
        print(f"Now it's round {num}")
        print(f"we have found {len(content)} downloadable books")
