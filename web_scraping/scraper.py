import requests
from bs4 import BeautifulSoup
import json



wiki = "https://en.wikipedia.org/wiki/History_of_Mexico"
response = requests.get(wiki)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')
result = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')


def get_citations_needed_count(result):
     return len(result)

def get_citations_needed_report(result):
    report=[]
    for i in range(len(result)):
        paragraph=result[i].parent.parent.parent.getText().strip()
        report.append({'Citation number': i+1 , 'paragraph' :paragraph})
    return report

json_data = json.dumps(get_citations_needed_report(result))
with open('json_data.json','w') as file:
    file.write(json_data)


if __name__=="__main__":
    count_citation=get_citations_needed_count(result)
    print(count_citation)
    report=get_citations_needed_report(result)
    # for string in report:
    #     print(f'Citation number {string["Citation number"]} : {string["paragraph"]}' )
    
    print(report[0])