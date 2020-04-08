import requests
from bs4 import BeautifulSoup


# max page를 추출하는 함수
def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.content, 'html.parser')
    pagenation = soup.find('div', {'class' : 'pagination'})
    links = pagenation.find_all('a')
    
    pages = []
    for link in links[:-1]:
        pages.append(int(link.text))
        
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find('div', {'class' : 'title'}).find("a")['title']
    company = html.find("span", 'company')
    company_anchor = company.find('a')
    location = html.find('div', {'class' : 'location'})
    if company.find('a') is not None:
        company = (str(company_anchor.string))
    else:
        company = (str(company.string))
    company = company.strip()
    location = html.find('div', {'class' : 'recJobLoc'})['data-rc-loc']
    job_id = html['data-jk']
    return {'title' : title ,
             'company' : company,
             'location' : location,
             "link": f"https://www.indeed.com/viewjob?jk={job_id}" }

def extract_jobs(last_page, URL, LIMIT):
    jobs = []
    for page in range(last_page):
        print (f"Indeed scrappying page number {page + 1}")
        result = requests.get(f"{URL}&start={page* LIMIT}")
        soup = BeautifulSoup(result.content, 'html.parser')
        results = soup.find_all('div', {'class' : 'jobsearch-SerpJobCard'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    LIMIT = 50
    URL = f"https://kr.indeed.com/jobs?q={word}&sort=i&limit={LIMIT}"
    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL, LIMIT)
    return jobs

