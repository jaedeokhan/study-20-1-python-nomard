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


















