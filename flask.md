## 4.0 Welcome to 2020 Update
* flask -> python으로 웹사이트를 만들 수 있게 해주는 micro-framework
* micro는 많은 설정을 하지 않고도 가능하다는 것이다.
* scrapper를 웹 서버에 넣는 작업을 한다. 
* 모두가 접근이 가능한 웹사이트를 만들고 , 언어들을 입력하면 그 언어에 맞는 직업들을 보여주는 것을 한다.
* 그리고, 사용자가 다운로드를 원하면 다운로드를 할 수 있게 만들어준다.

## 4.1 Introduction to Flask
* pip install flask
* flask를 사용하는 방법

> @app.route('/') => 현재 경로에 app.route()를 하면 밑에서 작성해준 함수를 제일 먼저 찾는다. 그래서 페이지에 들어가면 저렇게 되있다.
```python
from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return 'Hello! Welcome to mi casa!'

# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
@app.route("/contact")
def potato():
    return "Contact me!"

app.run(host="127.0.0.1") # 127.0.0.1 은 localhost이다. repl.it을 사용하려면 0.0.0.0 을 사용해야한다.
```

## 4.2 Dynamic URLs and templates
* 코드 자동정렬 -> Ctrl + K + F
* 현재 해야하는 것은 job search input form을 만들어주는 것이다.
* from flask import Flask, render_templeate 함수를 사용해서 potato.html을 불러온다.
* template 함수는 templates 폴더안에 있는 html에 접근하기에 생성해주고 그 안에 저장해야한다.
* 해결 url -> https://stackoverflow.com/questions/32140116/python-wsgi-flask-render-template-500-internal-server-error

> templates/potato.html => 요놈은 언어를 검색하면 직업이 나오게 하는 방법
```python
<!DOCTYPE html>
<html>
<head>
    <title>Job Search</title>
</head>
<body>
    <h1>Job Search</h1>
    <form>
        <input placeholder='Search for a job' required />
        <button>Search</button>
    </form>
</body>
</html>
```

> Flask, render_template 모듈을 사용해서 potato.html을 불러오기. => render_template("potato.html")을 불러온다.
```python
from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"


app.run(host="127.0.0.1")
```

## 4.3 Forms and Query Argumnents
* potato.html word 라는 인자를 get 방식으로 취하게 만들기 
    * .ipynb 파일에서는 처리하기
* report.html를 만들어서 query를 수행하면 이동하게 만들기
> potato.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Search</title>
</head>
<body>
    <h1>Job Search</h1>
    <form action="/report" method="get">
        <input placeholder='Search for a job' required name="word" />
        <button>Search</button>
    </form>
</body>
</html>
```

> report.html
* searchingBy 라는 인자는 flask에서 word를 처리해줘서 받는다.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Search</title>
</head>
<body>
    <h1>Search Results</h1>
    <h3>You are looking for {{searchingBy}}</h3>
    {{potato}}
</body>
</html>

```

> flask
* report로 넘어가면 word에 request.args.get('word')로 word를 입력하면 render_template함수를 사용해서 report.html에 두 개의 인자를 전달하기.
```python
from flask import Flask, render_template, request

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", 
                          searchingBy=word, potato="sexy")


app.run(host="127.0.0.1")
```

## 4.4 Scrapper Integration
* 저번에 만든 indeed, stackoverflow와 현재 만든 flask를 합치기
* 합치기전에 해결해야 할 것!
    * flask에서 word에 PYTHON이라고 대문자를 입력해도 소문자(lower)로 나오게 하기
    * report단에서 아무것도 입력하지 않으면 에러가 나오니 안나오게 수정해주기
* indeed.py를 -> scrapper.py 로 이름을 바꿔서 저장하고, flask에서 모듈로 불러와서 사용해서 처리해보기
    * 여기서 계속 에러가 나온 이유는 report.html에서 전에 테스트를 한다고 sexy를 {{potato}}로 받고 있어서 진행되지 못했음.

> flask, word 대문자를 소문자로 처리, report 단에서 아무것도 입력하지 않으면 에러가 나오니 안나오게 수정!
> 그리고, 아무것도 입력을 하지 않았을때 flask의 redirect의 모듕을 이용해서 /인 처음으로 redirect해주기
```python
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
    else:
        return redirect('/')
    return render_template("report.html", 
                          searchingBy=word)


app.run(host="127.0.0.1")
```

> scrapper.py의 get_jobs()를 이용해서 jobs가 받고 print(jobs)를 실행해보기
```python
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print (jobs)
    else:
        return redirect('/')
    return render_template("report.html", 
                          searchingBy=word)


app.run(host="127.0.0.1")
```

## 4.5 Faster Scrapper
* 매 번 크롤링해서 서버단에서 기다리게하는 비효율적인 방법을 사용할 수 없으니 가짜 DB를 만든다.
* fake DB는 항상 route 밖에 만들어야한다. 왜냐하면 안에 만들면 계속해서 다시 시작하기 때문이다. 
* report.html에서 jobs의 갯수를 resulstsNumber로 받아서 총 몇 개가 requsts 되는지 확인한다.

> flask -> db ={} 추가, if-else 문으로 db에 word가 있는지 없는지 체크 처리
```python
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# FAKE DB
db = {}

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromDB = db.get(word)
        if fromDB:
            jobs = fromDB
        else:
            jobs = get_jobs(word)
            db[word]= jobs
    else:
        return redirect('/')
    return render_template("report.html", 
                          searchingBy=word, resultsNumber=len(jobs))


app.run(host="127.0.0.1")
```

> report.html 에 resultsNumber를 만들어서 flask에서 len(jobs)을 받은 것을 처리하기.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Search</title>
</head>
<body>
    <h1>Search Results</h1>
    <h3>Found {{resultsNumber}} results for: {{searchingBy}}</h3>
</body>
</html>
```

## 4.6 Rendering Jobs!
* rendering 을 searchingBy=word, resultsNumber=len(jobs), jobs=jobs 세 개를 처리해주기.
* 그리고, 테이블로 jobs를 보여줄 수 있게 report.html에 table을 만들기 -> section을 grid로 처리하기
    * report.html에 렌더링을 할때는 flask에서 처리가 가능한 <% for job in jobs %> 와 같이 <%%> 안에 처리를 해줘야한다.
> 1. rendering으로 report.html에서 받기
```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Search</title>
    <style>
        section {
            display : grid;
            gap:20px;
            grid-template-columns: repeat(4, 1fr);
        }
    </style>
</head>
<body>
    <h1>Search Results</h1>
    <h3>Found {{resultsNumber}} results for: {{searchingBy}}</h3>
    <section>
        <h4>Title</h4>
        <h4>Company</h4>
        <h4>Location</h4>
        <h4>Link</h4>
        {% for job in jobs %}
            <span>{{job.title}}</span>
            <span>{{job.company}}</span>
            <span>{{job.location}}</span>
            <a href="{{job.link}}" target="_blank">Apply</a>
        {% endfor %}
    </section>
</body>
</html>
```

> 2. flask에서 처리 -> 저번 강의와 동일
```python
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# FAKE DB
db = {}

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word]= jobs
    else:
        return redirect('/')
    return render_template("report.html", 
                          searchingBy=word,
                          resultsNumber=len(jobs),
                          jobs=jobs)


app.run(host="127.0.0.1")
```

## 4.7
* 사용자가 이것을 csv파일로 저장을 가능하게 만들기
    * csv로 export&저장하는 기능 생성하기
* 새로운 route를 하나 만들어서 try-exception으로 raise Exception을 발생시키기
* report.html에서 a태그로 검색한 페이지를 export를 가능하게 연결해주는 a 태그 생성

> 1. flask 에서 app.route('export')를 추가 생성
```python
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# FAKE DB
db = {}

@app.route("/")
def home():
    return render_template("potato.html")
# @는 decorate , 요 놈은 바로 밑에 함수를 찾기 때문에 무조건 함수로 작성을 해준다.
# /<username> 으로 동적 URL을 구성이 가능하다.
# @app.route("/<username>")
# def potato(username):
#     return f"Hello your name is {username} how are you doing"

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word]= jobs
    else:
        return redirect('/')
    return render_template("report.html", 
                          searchingBy=word,
                          resultsNumber=len(jobs),
                          jobs=jobs)

@app.route("/export")
def export():
    try: # word를 얻어오고, 만약 word가 없다면 redirect로 초기 화면으로 보내고, word가 있다면 소문자로 모두 바꿔주고, jobs에 담는다.
        word = request.args.get('word')
        if not word: # 
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect('/')
    
    
app.run(host="127.0.0.1")
```












