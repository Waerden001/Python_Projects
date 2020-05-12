# Guggenheim, Met, Getty Art Books 

### Motivation and goal
The Guggenheim Museums and Foundation, the Metropolitan Museum of Art and the Getty provide **free** online Arxives of amzing art publications.
- [Guggenheim Internet Arxive](https://archive.org/details/guggenheimmuseum)
- [MetPublications](https://www.metmuseum.org/art/metpublications/titles-with-full-text-online?searchtype=F)
- [The Getty Virtual Library](https://www.getty.edu/publications/virtuallibrary/index.html)
We didn't find a bottom to download all books with one click, but it's tedious and almost impossible to download them one by one. 
We thought it's a good chance to write some simple python web scraping code to do the job for us. 

## Approach
The basic idea is to ultilize python packages 
- ```requests```,
  - e.g. ```urls = ["...pg=1", "...pg=2", ...]```, find a way to get all urls in the arxiv or online library
  - e.g. ```res=requests.get(url)``` load each relevant page
- ```bs4``` 
  - e.g. ```soup = bs4.BeautifulSoup(res.text)```, parse the text content of the HTML file
  - e.g. ```book_elem = soup.find_all("div", class_="item-ttl")```,find all blocks with links/hrefs to books(or their downloading page) needed
- ```os``` or ```urllib.request```
  - ```os```, write ```res.content```, download directly in local folders
  - ```urllib.request``` , download to google drive. 

Different minor problems appear for these different libraries, check out the corresponding jupyter notebooks to see the specific solutions. 
### Guggenheim Museum
- Some links don't contain any .pdf files

### Metropolitan Museum of Art

- Links force the browser to download the pdf directly instead of opening the pdf in a new tab
- Some links don't contain any .pdf files, or the html block that we're looking for

### The Getty Museum
- The website is dynamic, bs4 selenium don't work.


Remarks
- Request fail in Jupyter notebook but success in google colab
- Download fail in Jupyter notebook but success in google colab
- Connect google colab to local run time
- [Cancel google drive subscriptions](https://play.google.com/store/account/subscriptions)
- [Connect google colab to local run time](https://research.google.com/colaboratory/local-runtimes.html)


References:

- [Automate the boring stuff](https://automatetheboringstuff.com/chapter11/)
