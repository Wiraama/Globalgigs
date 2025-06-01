from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests


session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)


def get_gig_jobwebkenya(pages=40):
    jobs = []
    count = 0
    for page in range(1, pages + 1):
        url = f"https://jobwebkenya.com/jobs/page/{page}/"
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #with open(f'dsta_{page}.html','w') as f:
            #f.write(str(soup))
        job_cards = soup.find_all('li', class_="job")
        for card in job_cards:
            title_tag = card.find('div', id="titlo")
            link_tag = title_tag.a['href']
            about_tag = card.find('div', id="exc")
            if title_tag and link_tag and about_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag
                about = about_tag.get_text(strip=True)
                
                job = {
                    "title": title,
                    "link": link,
                    "about": about
                }
                count += 1
                jobs.append(job)
    print(f"Jobwebkenya added {count} jobs")
    return jobs