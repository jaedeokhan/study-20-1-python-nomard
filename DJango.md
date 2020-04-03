## 3.0 Django is AWESOME

## 3.1 *args **kwargs => argument, keyword argunment
* Django 에는 이해해야 할 두 가지 컨셉이 있다. => 위의 두개와 그리고 객체지향 프로그래밍의 상속
* print(1,1,1,1,1,1,1,11,1,1,1,1,1,1,1)와 같이 인자를 무한으로 받아서 출력이 가능하게 할려면? Django에서는 이러한 기능을 많이 사용한다.
  * 두 가지 방법
    * -> *args
    * position argument => *args
    * keyword argument -> hello=True, aa=True => **kwargs

> position argument
```python
def plus(a,b, *args):
    print (args)
    return a + b

plus(1,2, 1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6) , print(args)를 하면 print함수와 같이 무한대로 쓰는것이 가능하고, tuple형태로 받는다.
# 3
```

> keyword argument
```python
def plus(a, b, *args, **kwargs):
    print (args, kwargs)
    return a + b

plus(1,2,3,4,5,6,7,8,9,10, eh=True, ff=False)
# (3, 4, 5, 6, 7, 8, 9, 10) {'eh': True, 'ff': False} , **kwargs 를 추가하면 딕셔너리 형태로 데이터를 가지게 된다.
# 3
```

## 3.2 Intro to Object Oriented Programming
* blueprint  == class => instance는 class의 결과물
> Car class를 만들어서, 두 개의 차량에 객체를 담아주고, color라는 차의 객체의 속성응로 색깔을 입력해주기
```python
class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4
    
porche = Car()
porche.color = 'Red'

ferrai = Car()
ferrai.color = 'Yellow'

mini = Car()
mini.color = 'White'
```

## 3.3 Methods part one
* Car() 색을 위의 방법으로 계속해서 바꾸는 방법은 비효율적이다. functions으로 만들어서 class의 self.변수를 받으면 된다.
* functions 과 methods의 차이는? class안에 있으면 methods이고, 밖이면 functions이다.
* python mehtod는 하나의 argument랑 함께 사용을 한다. 
* self란? -> method를 호출하는 instance 자신이다.
* python은 method를 호출할 때 그 method의 instance를 첫 번째 argument로 사용한다.
```python
class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4
    def start(self):
        print (self.doors) # self를 사용하면 장점이 있다. self말고 다르게 potato나 아무거나 하나는 꼭 있어야 한다.
        print ("I started")
        
porche = Car()
porche.color = 'Red'
porche.start()

```

## 3.4 Methods part Two
* print (dir(Car) 을 하면 Car 객체의 dir을 출력을 하면 class 안에 있는 모든 것들을 리스트로 보여준다.
* Override(재정의)

```python
class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    def __str__(self):
        return 'lalalalalla'
        

# dir 은 class안에 있는 모든 것들을 리스트로 보여준다.
# print (dir(Car))
porche = Car()
print (porche) # lalalalalla
```
* methods == __init__() 과 동일하다.

> __init__() 이 메서드와 동일하다. 그래서 처음에 __init__을 사용하면 초기 세팅이 가능하다. Car()를 호출할때 인자를 주는게 가능하다.
```python
class Car():    
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"
    

# dir 은 class안에 있는 모든 것들을 리스트로 보여준다.
# print (dir(Car))
porche = Car(color="green", price="$40")
print (porche.color, porche.price) # green $40

mini = Car()
print (mini.color, mini.price) # black $20 , 요 놈들응 초기에 설정을 해주지 않아서 값이 __init__에서 설정해준것이 들어간다.
```
## 3.5 Extending Classes
* class를 어떻게 extend 하는지 배운다.
* super class는 부모 클래스이다.
* super class 는 내가 extend 했던 그 class이다.

> 슈퍼카와 같은 오픈 문인 함수를 추가를 해주고 싶은데 , 오픈카와 같은 차는 많이 없는데 위의 Car클래스에서 함수를 사용하면 비효율적이다.
```python
# 위에서 take_off를 하는 문을 여는 차량은 한정적인데 위의 클래스에서 가지고 있는 것은 비효율적이다.
class Convertible():    
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"
    
    def take_off(self):
        return "taking off"
    
porche = Convertible(color="green", price="$40")
porche.take_off() # 'taking off'
```

> inherit 즉 상속을 해준다. 그리고 extend 기능을 사용하기 위해서는 super를 사용한다.
```python
# inherit , extend
class Convertible(Car):

    def __init__(self, **kwargs):
        # super를 통해서 부모 클래스에 접근이 가능하다.
        super().__init__(**kwargs)
        self.time = kwargs.get('time', 10) 
        
        
    def take_off(self):
        return "taking off"
    
    # Override
    def __str__(self):
        return f"Car with no roof"

class Something(Convertible):
    pass

porche = Convertible(color="green", price="$40")
print (porche.color) # green
```

## 3.6 Whats Next
Long Live Python


 
