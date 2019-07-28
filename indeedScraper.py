# import libraries
from bs4 import BeautifulSoup
import urllib.request

#########################
# Import Custom Modules #
#########################
# Define module path
import sys
# Insert at 1
sys.path.insert(1, 'Path to Modules folder')
# Custom Modules
from availableJobs import availableJobs
from companyNames import companyNames
from dateCreated import dateCreated
from jobLocation import jobLocation
from jobSalary import jobSalary
from descriptionSummary import descriptionSummary
from outputHeaders import *

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

# Execute function => companyNames
print(hAJ)
availableJobs(parsedHTML)
print(hCN)
companyNames(parsedHTML)
print(hDC)
dateCreated(parsedHTML)
print(hJL)
jobLocation(parsedHTML)
print(hJS)
jobSalary(parsedHTML)
print(hDS)
descriptionSummary(parsedHTML)
