# Function - iterate through div and span elements for value and output to list
def dateCreated(parsedHTML):
    dates = []
    for div in parsedHTML.find_all(name='div', attrs={'class':'result-link-bar'}):
        for span in div.find_all(name='span', attrs={'class':'date'}):
            dates.append(span.getText().strip())
    print(dates)
