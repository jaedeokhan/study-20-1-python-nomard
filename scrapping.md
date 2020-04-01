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





## 2.6 Extracting Titles















