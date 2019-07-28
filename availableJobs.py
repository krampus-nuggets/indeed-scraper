# Function - iterate through div and a elements for value and output to list
def availableJobs(parsedHTML):
    jobs = []
    for div in parsedHTML.find_all(name='div', attrs={'class':'title'}):
        for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
            jobs.append(a.getText().strip())
    print(jobs)
