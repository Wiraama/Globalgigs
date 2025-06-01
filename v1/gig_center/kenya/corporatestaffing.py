from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}

def get_gig_corporatestaffing(pages=10):
    jobs = []
    count = 0
    for page in range(1, pages + 1):
        url = f"https://www.corporatestaffing.co.ke/jobs/page/{pages}/"
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('article')
        
        for card in job_cards:
            try:
                title_tag = card.find('h2', class_='entry-title')
                if not title_tag or not title_tag.a:
                    continue
                link = title_tag.a['href']
                about = card.find('div', class_='entry-summary')
                    
                job = {
                    "title": title_tag.a.get_text(strip=True),
                    "about": about.p.get_text(strip=True) if about and about.p else "No Description Found",
                    "link": link
                    }
                count += 1
                jobs.append(job)
            except Exception as e:
                print(f"Skipping becouse of error {e}")
                continue
    print(f"Corporatestaffing added {count} jobs")
    return jobs