from bs4 import BeautifulSoup
import requests

url = 'https://www.brightermonday.co.ke/jobs'
headers = {'User-Agent': 'Mozilla/5.0'}

def get_gig_brightermonday(pages=10):
    jobs = []
    count = 0
    
    #print(job_cards)
    for page in range(1, pages + 1):
        url = f"https://www.brightermonday.co.ke/jobs?page={pages}/"
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.select('div.flex.flex-wrap.col-span-1.mb-5.bg-white.rounded-lg.border.border-gray-300.hover\\:border-gray-400')
        
        for card in job_cards:
            title_tag = card.select_one('[data-cy="listing-title-link"] p')
            company_tag = card.select_one('a[href*="/jobs?q="]')
            function_tag = card.find('p', string=lambda t: t and 'Job Function' in t)
            badges = card.select('.text-loading-hide')
            posted = card.find('p', string=lambda t: t and 'ago' in t)
            link_tag = card.find('a', class_=[
                'relative',
                'mb-3',
                'text-lg',
                'font-medium',
                'break-words',
                'focus:outline-none',
                'metrics-apply-now',
                'text-link-500',
                'text-loading-animate'
            ])
            if badges:
                location = badges[0].text.strip()
                type = badges[1].text.strip()
                salary = badges[2].text.strip()
            else:
                location = 'N/A'
                type = 'N/A'
                salary = 'N/A'
            # Job Function
            if function_tag:
                function = function_tag.text.replace('Job Function', '').strip().lstrip(':').strip()
            else:
                function = 'N/A'
                
            if title_tag:
                job = {
                    "title": title_tag.text.strip() if title_tag else 'N/A',
                    "about": company_tag.text.strip() if company_tag else 'N/A',
                    "link": link_tag['href']
                }
                count += 1
                jobs.append(job)
    print(f"brightermonday added {count} jobs")
    return jobs