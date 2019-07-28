# Function - iterate through div and span elements for value and output to list
def companyNames(parsedHTML):
    names = []
    for div in parsedHTML.find_all(name='div', attrs={'class':'sjcl'}):
        for span in div.find_all(name='span', attrs={'class':'company'}):
            names.append(span.getText().strip())
    print(names)
