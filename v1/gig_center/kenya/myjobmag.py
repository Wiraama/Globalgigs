from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}

"""with open('dsta.html','w') as f:
    f.write(str(soup))"""
    
def get_gig_myjobmag(pages=3):
    jobs = []
    count = 0
    for page in range(1, pages + 1):
        url = f"https://www.myjobmag.co.ke/jobs/page/{pages}"
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        """with open('dsta.html','w') as f:
            f.write(str(soup))"""
        job_cards = soup.find_all('li', class_='job-list-li')
    
        for card in job_cards:
            try:
                title_tag = card.find('h2')
                if not title_tag or not title_tag.a:
                    continue
                link_tag = title_tag.a['href']
                about = card.find('li', class_='job-desc')
                    
                job = {
                    "title": title_tag.a.get_text(strip=True),
                    "about": about.get_text(strip=True) if about and about else "No Description Found",
                    "link": "https://www.myjobmag.co.ke" + link_tag
                    }
                count += 1
                jobs.append(job)
            except Exception as e:
                print(f"Skipping becouse of error {e}")
                continue
    print(f"Myjobmag added {count} jobs")
    return jobs