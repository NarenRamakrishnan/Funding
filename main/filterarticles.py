Keywords = ["funding", "raises", "million", "billion", "seed", "series", "venture", "investment", "backed", "round"]


def filter_urls(urls):
    """
    Filter a list of URLs to only include those about funding.

    param urls: List of URLs (strings) to filter
    return: A list of URLs that contain at least one numeric character
    """
    return [url for url in urls if any(key in url.lower() for key in Keywords)]


