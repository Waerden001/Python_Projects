import requests
import bs4
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib.request


def get_links_by_feature(url, soup_feature, tag, attr="href", base_link=""):
    """
    :param: url, list,list of all the pages in the library
    :param: soup_feature: list of strings, the BeautifulSoup feature to select the block we need, e.g. ["div", "class_="item-ttl"] 
    #TODO: send parameters to soup better 
    :param: tag, str, the concrete tag name in the block, e.g. "a"
    :param: attr, str, the exact attr contains the information we need, e.g. "href"
    """
    book_list = []
    for link in url: 
        res = requests.get(link)
        soup = bs4.BeautifulSoup(res.text)
        book_elem = soup.find_all(soup_feature)
    for ele in book_elem:
        book_list.append(base_link+ele.find(tag)[attr])
    return book_list

#TODO: This function is a little bit redundant, we should use get_links_by_feature again to get all direct .pdf links 
def download_from_html(book_list,folder_location, link_description="a[href$='.pdf']"):
    """
    :param: book_list, list of strs, list of all links to the html pages that contain the pdf files directly
                                    e.g. https://archive.org/details/braque00braq
    :param: foler_location, str, location of the folder, e.g. "C:\\User\\Waerden\\Desktop"
    :param: link_description: str, css features to get the pdf links, e.g. "a[href$=.pdf]" 
    """
    if not os.path.exists(folder_location):os.mkdir(folder_location)
    count = 0
    for book in book_list:
        count += 1
        response = requests.get(book)
        soup= BeautifulSoup(response.text, "html.parser")     
        for link in soup.select(link_description):
            #Name the pdf files using the last portion of each link which are unique in this case
            book_name = link['href'].split('/')[-1]
            filename = os.path.join(folder_location,book_name)
            print(f"Downloading book {count}: {book_name}")
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(book,link['href'])).content)
                print(f"Download book {count}: {book_name} complete!")
              

def download_from_pdf_link(content, folder_location):
    """
    :param: content, list of strs, a list contains all direct links to the pdf files(or any directly downloadable files),
                                 e.g.http://d2aohiyo3d3idm.cloudfront.net/publications/virtuallibrary/0892369426.pdf
    :param: folder_location: str, goodle drive location that you want to store all the downloaded files, e.g. "./drive/My Drive/MetMuseum/"
    """
    num = 1
    for url in content:
        name = url.rsplit('/',1)[-1]
        filename = folder_location+name
        print(f"Downloading book {num}: {name},start!")
        urllib.request.urlretrieve(url, filename)
        num += 1
        print(f"Download book {num}: {name},complete!")