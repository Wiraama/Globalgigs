import requests
from bs4 import BeautifulSoup

def get_gig():
    url = 'https://remoteok.com/remote-dev-jobs'
    headers = {'User-Agent': 'Mozilla/5.0'}

    message = []

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = soup.find_all('tr', class_='job')  # job posts are in <tr class="job">

    for job in jobs:
        title_tag = job.find('h2')
        company_tag = job.find('h3')
        job_link = job.get("data-href")
        link = "https://remoteok.com" + job_link
        if title_tag and company_tag:
            title = title_tag.text.strip()
            company = company_tag.text.strip()
            link = link
            mes = {
                    'title': title,
                    'company': company,
                    'link': link
                    }
        message.append(mes)

    return message
