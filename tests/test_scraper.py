from web_scraping.scraper import get_citations_needed_count, get_citations_needed_report
import requests
from bs4 import BeautifulSoup
import pytest



def test_get_citations_needed_count():
    wiki = "https://en.wikipedia.org/wiki/History_of_Mexico"
    response = requests.get(wiki)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    result = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')
    assert get_citations_needed_count(result) == 5
    
def test_get_citations_needed_report(): 
    wiki = "https://en.wikipedia.org/wiki/History_of_Mexico"
    response = requests.get(wiki)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    result = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')
    report=get_citations_needed_report(result)
    assert report[0]== {'Citation number': 1, 'paragraph': 'The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.'}
    
    
    

