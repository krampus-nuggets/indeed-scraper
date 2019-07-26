# import libraries
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

# Create list
summaries = []

# Function - iterate through div elements for value and output to list
def descriptionSummary(parsedHTML, summaries):
    for divParent in parsedHTML.find_all(name='div', attrs={'class':'result'}):
        for divChild in divParent.find_all(name='div', attrs={'class':'summary'}):
            summaries.append(divChild.getText().strip())
    print(summaries)

# Execute function => descriptionSummary
descriptionSummary(parsedHTML, summaries)
