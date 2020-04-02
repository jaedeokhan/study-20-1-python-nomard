# Python scrapy 

## 2.0 What is Web Scrapping
웹 스크래퍼란 웹 페이지 HTML, CSS, Javascript 등 웹 페이지에 있는 모든 내용들을 가져올 수 있는 기법이다.

## 2.1 what are We Building
이번 프로젝트는 나는 파이썬을 개발하기 위한 개발자이고, 가장 유명한 구인구직 사이트 중에 하나인 Indeed라는 곳에서 데이터를 긁어오는 것이다.

## 2.2 Navigating with Python
1. url 접근
2. page 갯수 파악
3. import requests
4. from bs4 import BeautifulSoup
```python
import requests
from bs4 import BeautifulSoup

indeed_url = requests.get('https://kr.indeed.com/jobs?q=python&limit=50')

print (indeed_url) # status 200
```

## 2.3 Extracting Indeed Pages
* pagenation 을 가져오기. 
* find() 함수는 하나만 가져온다.
* find_all() 함수는 전체를 가져온다. -> list형태로
* select_one() 하나만 가져오기 가능
* select() 도 전체를 가져온다.
* list를 하나 만들어서 for문을 돌려서 .append()함수를 사용해서 저장하기.
```python
import requests
from bs4 import BeautifulSoup

indeed_url = requests.get('https://kr.indeed.com/jobs?q=python&limit=50')

soup = BeautifulSoup(indeed_url.content, 'html.parser')

pagenation = soup.find('div', {'class' : 'pagination'})

pages = pagenation.find_all('a')

spans = []
for page in pages:
    spans.append(page.find('span'))

# 처음부터 -1까지 즉 맨 마지막은 빼고 출력을 한다.
print (spans[:-1]) # [<span class="pn">2</span>, <span class="pn">3</span>, <span class="pn">4</span>, <span class="pn">5</span>,<span class="pn">6</span>, <span class="pn">7</span>, <span class="pn">8</span>, <span class="pn">9</span>, <span class="pn">10</span>ㅁㄴㅇ
```

## 2.4 Extracting Indeed Pages part Two
* pagenation 의 max_page를 찾아보기

## 2.5 Requsting Each Page
* pagenation을 max_page requests하는 방법을 찾아보기
* last page인 10을 추출하기 위한 함수로 만들어준다 -> extract_indeed_page()
* last page인 갯수를 받아서 &start=갯수 설정해서 출력하는 함수를 만들어준다. -> extract_indeed_jobs()

> max_page의 수를 출력하는 함수
```python
def extract_indeed_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.content, 'html.parser')
    pagenation = soup.find('div', {'class' : 'pagination'})
    links = pagenation.find_all('a')
    
    pages = []
    for link in links[:-1]:
        pages.append(int(link.text))
        
    max_page = pages[-1]
    return max_page
```

> last_page 의 숫자를 받아서, &start= 갯수 설정해서 출력하는 함수
```python
def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.content, 'html.parser')
        job_titles = soup.select('a.jobtitle.turnstileLink')
        for index, job_title in enumerate(job_titles):
            jobs.append(job_title.text.replace('\n', ''))
    return jobs

last_indeed_pages = extract_indeed_page() # last_page = 10 이라면

extract_indeed_jobs(last_indeed_pages) # 모든 title을 출력
```
## 2.6 Extracting Titles
* find("a")["title"] a 태그의 title에 바로 접근해서 데이터를 가져오기.
```python
def extract_indeed_jobs_2(last_page):
    jobs = []
    result = requests.get(f"{URL}&start={0* LIMIT}")
    soup = BeautifulSoup(result.content, 'html.parser')
    results = soup.find_all('div', {'class' : 'jobsearch-SerpJobCard'})
    for result in results:
        title = result.find('div', {'class' : 'title'}).find("a")['title']
        print (title)
#     return jobs

# last_indeed_pages = extract_indeed_page()

extract_indeed_jobs_2(last_indeed_pages) # title들이 쭉 나온다.
```

## 2.7 Extracting Compaines 
* 회사 이름의 데이터를 가져오기 -> div.sjlc > span.company
```python
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_jobs_2(last_page):
    jobs = []
    result = requests.get(f"{URL}&start={0* LIMIT}") # 일단은 여기서 테스트를 위해 1페이지만 가져오기
    soup = BeautifulSoup(result.content, 'html.parser')
    results = soup.find_all('div', {'class' : 'jobsearch-SerpJobCard'})
    for result in results:
        title = result.find('div', {'class' : 'title'}).find("a")['title'] # company_title에 title 속성으로 가져오기.
        company = result.find("span", 'company')  # 먼저, span에 company를 가져오기
        company_anchor = company.find('a') # 여기서 company에 a 태그를 담는 이유는, span > a 태그에 데이터가 들어가 있는 경우도 존재
        if company.find('a') is not None: # a 태그에 비어있지 않다면, span > a 에 있는 company_anchor를 가져오기
            company = (str(company_anchor.string))
        else: # 아니면 , company 에 있는 span.company에서 가져오기. 
            company = (str(company.string))
        company = company.strip() # whitespace가 존재하기 때문에, replace로 제거 가능하지만, strip()으로 하면 더 쉽다.
        print (title, company) # title, company_name 이 나오는지 테스트!
#     return jobs

# last_indeed_pages = extract_indeed_page()

extract_indeed_jobs_2(last_indeed_pages)
```

## 2.8 Extracting Locations and Finishing up
* 정리
    * extract_indeed_page() 함수로, max_page 즉 last_page를 가져오는 함수를 만들고,
    * extract_job(html) 함수로, 인자로 result를 받아서, extract_indeed_job_2 의 for문에 작성해주기.
    * extract_indeed_jobs_2(last_page), 첫 번째 max_page 를 뽑아주는 함수에게 last_page를 받고, for문에서는 extract_job(html) 에 result를 넣어주고, 데이터를 jobs라는 []리스트에 담아주기
    















