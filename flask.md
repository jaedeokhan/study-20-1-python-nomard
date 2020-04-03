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

