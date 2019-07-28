# Function - iterate through div elements for value and output to list
def descriptionSummary(parsedHTML):
    summaries = []
    for divParent in parsedHTML.find_all(name='div', attrs={'class':'result'}):
        for divChild in divParent.find_all(name='div', attrs={'class':'summary'}):
            summaries.append(divChild.getText().strip())
    print(summaries)
