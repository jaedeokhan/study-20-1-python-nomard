import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i&pg="

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.content, 'html.parser')
    pages = soup.find('div', {'class' : 's-pagination'}).find_all('a')
#     pages = soup.select('a.s-pagination--item span')
    pages = int(pages[-2].text) # get_text(strip=True) 로도 whitespace 제거가 가능
    return pages

def extract_job(html):
#     title = html.select_one('div.-grid--cell.fl1 h2 a')
    title = html.find('div', {'class' : 'grid--cell fl1'}).find('h2').find('a')['title']
    title = title.replace('-', '')
    # span 안에 span이 있는 구문이 존재하면 recursive=False로 접근하지 않게 하는 것도 가능하다.
    # python 의 unpacking value 기능이다.
    # span의 첫 번째 요소에는 company를 담고, span의 두 번째 요소에는 location을 담는다.
    company, location = html.find('div', {'class' : 'grid--cell fl1'}).find('h3').find_all('span', recursive=False)
    company = company.get_text(strip=True) # strip('-') 와 같이 replace와 같은 기능을 한다.
    location = location.get_text(strip=True).replace(',', '') # 맥에서 \n은 \r 일수도 있음
    job_id = html['data-result-id']
    return {'title' : title, 'company' : company, 'location' : location,
           'link' : f'https://stackoverflow.com/jobs/{job_id}'}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        if page == 8:
            break
        print (f'Stackoverflow scrappying page number {page + 1}')
        result = requests.get(f"{URL}{page + 1}") # page + 1
        soup = BeautifulSoup(result.content, 'html.parser')
        results = soup.find_all('div', {'class' : '-job'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
