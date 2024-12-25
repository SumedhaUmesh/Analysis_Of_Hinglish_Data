from scraper import scrapeInsta
from imageDownloader import saveImage


def scrape(url):
    post_url = url.replace('?utm_source=ig_web_copy_link', '?__a=1')
    media_links = scrapeInsta(post_url)
    saveImage(media_links)
