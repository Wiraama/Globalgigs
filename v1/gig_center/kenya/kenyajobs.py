from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
    
def get_gig_kenyajobs(pages=1):
    jobs = []
    count = 0
    for page in range(1, pages + 1):
        url = f"https://www.kenyajob.com/job-vacancies-search-kenya?page={pages}"
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        """with open('dsta.html','w') as f:
            f.write(str(soup))"""
        job_cards = soup.find_all('div', class_="card-job-detail")
        for card in job_cards:
            try:
                title_tag = card.find('h3')
                if not title_tag or not title_tag.a:
                    continue
                link = card.get('data-href')
                about = card.find('p')
                    
                job = {
                    "title": title_tag.a.get_text(strip=True),
                    "about": about.get_text(strip=True) if about and about else "No Description Found",
                    "link": link
                    }
                count += 1
                jobs.append(job)
            except Exception as e:
                print(f"Skipping becouse of error {e}")
                continue
    print(f"Kenyajobs added {count} jobs")
    return jobs