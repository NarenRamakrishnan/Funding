from newspaper import Article

def fetch_article_content(url):
    """
    Fetch and parse the article content from the given URL.

    param url: URL of the article to fetch
    return: A tuple containing the article title and text
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text or len(article.text.strip()) < 100:
            raise Exception("Article length too short for", url)
        
        return article.title, article.text
    
    except Exception as e:
        raise Exception("Error in fetching article content for", url)
