# Function - iterate through div and span elements for value and output to list
def jobSalary(parsedHTML):
    salaries = []
    for div in parsedHTML.find_all(name='div', attrs={'class':'salarySnippet'}):
        for span in div.find_all(name='span', attrs={'class':'salary'}):
            salaries.append(span.getText().strip())
            salaries = [hex.replace('\xa0',' ') for hex in salaries]
    print(salaries)
