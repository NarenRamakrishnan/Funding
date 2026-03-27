from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def article_links_from_category(CATEGORY_URL):
    """
    Finds all the urls present on the news website.

    param CATEGORY_URL: The url of the news website.
    return links: A list of the urls on the news website.
    """
    options = Options()
    options.headless = True  
    driver = webdriver.Chrome(options=options)

    driver.get(CATEGORY_URL)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


    links = set()
    for a in soup.find_all("a", href=True):
        href = a['href']
        full_url = urljoin(CATEGORY_URL, href)


        if urlparse(full_url).netloc != urlparse(CATEGORY_URL).netloc:
            continue

        if any(x in full_url for x in ["/category/", "/author/", "/tag/", "/privacy-policy/", "/about/", "/contact-us/", "/terms-of-use/"]):
            continue

        if full_url.rstrip("/") == CATEGORY_URL.rstrip("/"):
            continue
        links.add(full_url)

    driver.quit()

    return links

#CATEGORY_URL = "https://techfundingnews.com/category/us/"
#print(article_links_from_category(CATEGORY_URL))
