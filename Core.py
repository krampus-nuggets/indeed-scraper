# Indeed - Scraper v0.1
# Project scoped towards HTML Scraping not JavaScript
# Please check out Headless Browser libraries for Python such as Selenium for JavaScript Heavy Scraping
# This scraper WILL NOT work on JavaScript Heavy Websites

# import libraries
import bs4
from bs4 import BeautifulSoup
import urllib.request

# Specify the Scrape URL
# Test URL - https://www.indeed.co.za/jobs?q=wordpress&l=Cape+Town,+Western+Cape&start=10
pageURL =  '<your-url>'

# Assign User-Agent to Scrape Request
req = urllib.request.Request(
    pageURL,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Query webpage HTML Code and Assign to variable 'pageQuery'
pageQuery = urllib.request.urlopen(req)

# Parse the HTML Code using BeautifulSoup and assign parsed data to variable 'parsedHTML'
parsedHTML = BeautifulSoup(pageQuery, 'html.parser')
