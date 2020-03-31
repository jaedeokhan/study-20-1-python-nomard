# Python_Nomard
# 2020 03 30 Nomard Python Day 1

## Data Types of Python
### 1. Variable
어떤 종류의 것들을 우리가 변수에 넣을 수 있는가?
* Int => <class 'int'>
* Float => <class 'float'> 
* String of Text => <class 'str'>
* Boolean -> True , False => <class 'bool'>
* None -> Nothing => <class 'NoneType'>
* Dictonary
* tuple
* list
* Set

## 1.1 Lists in Python  -> List is mutable sequence
list -> implement common, mutable , mutable은 우리가 값을 변경할 수 있다는 것이다. immutable은 수정 불가능한이 뜻이고, 값을 변경 할 수 없다.
Python 에는 sequence type이 존재한다. sequence는 열거되어 있는거고, sequence는 list와 같은 것이다.
Python에는 두 개의 sequence type이 존재한다 -> list, tuple
만약? 월~일요일을 저장해야 한다면?

```python
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
print (type(days)) # list
print ('Mon' in days) # Ture, x in s
print (days[2]) # Wed, s[i]
print (len(days)) # 5, len(days)
# python에는 Document에 가면 다양한 값이 있다.
# s.append(x)
# s.clear()
# s.reverse()
```
## 1.2 Tuples and Dicts -> Immutable sequence
list는 Common and Mutable sequence operations 두 가지 모두 가능하다.
tuple은 common operations 만 가능하다. 데이터를 변경을 하고 싶지 않응 때 주로 사용한다.
tuple로 무엇을 할 수 있을까?
가끔 object와 reference를 가지고 싶다면? 

```python
# list, tuple은 다양한 값들을 가질 수 있다.
something_list = ['tntt', True, 12, None, False, 'laslaslas']
something_tuple = ('tntt', True, 12, None, False, 'laslaslas')

print (something_list) # ['tntt', True, 12, None, False, 'laslaslas']
print (something_tuple) # ('tntt', True, 12, None, False, 'laslaslas')
```

## 1.2.1 dictonary -> 사전과 같다 -> 즉 요놈은 list, boolean, tuple, arrange 모두 다양한 값들을 key, value 형태로 가진다.
```python
name = "Nico"
age = 29
korean = True
fav_food = ["Kimchi", "Sashimi"]

# dictonary -> key, value 
nico = {
    'name' : 'Nico',
    'age' : 29,
    'korean' : True,
    'fav_food' : ["Kimchi", "Sashimi"]
}

print (nico['name']) # Nico
print (nico['fav_food']) # '[Kimchi', 'Sashimi']

# nico dictonary에서 fav_food의  Kimchi를 가져오고 싶다면?
print (nico['fab_food'][0]) # 'Kinmchi'

# 새로운 데이터를 딕셔너리에 추가를 하고 싶으면?
nico['handsome'] = False
print (nico) # {'name': 'Nico', 'age': 29, 'korean': True, 'fav_food': ['Kimchi', 'Sashimi'], 'handsome': True}
```
## 1.3 Built-in Functions
### Python standard library -> 인터넷에 검색하면 Documents가 나온다.
python에는 기본적인 함수가 매우 다양하게 있다.
* len()
* sorted()
* type()
* print() 등등
```python
print(len('adfasdfasdfasdfasdfafasdf')) # 25
age = '18' 
print (type(age)) # str
print (type(int(age))) # int
```

## 1.4 Creating a Your First Python Function 
python 에서는 def를 감쌀때는 다른 언어처럼 { } 를 사용하지는 않는다.
python에서는 indentation(들여쓰기)로 문장의 시작과 끝을 판단을 한다.

```python
def say_hello():
    print ('hello world')
    print ('Bye')
    
say_hello()    
```

## 1.5 Function Arugments

```python
def printf(who):
    print ('hello ',who)

printf("Nicolas")  # hello  Nicolas
printf('deok') # hello deok
printf('nyeon') # hello nyeon
printf(type(1234)) # int
printf(type(True)) # bool

# default value
def plus(a,b = 0):
    print (a + b)
 
def minus(a,b):
    print (a - b)

print(plus(3)) # 3 
print(plus(5,3)) # 2 
```

## 1.6 Returns
Return 과 print의 차이는?  function에서는 Return 되어진 값이 치환이 되어진다.
reuturn을 하면 출력하고 종료한다.
```python
def p_plus(a,b):
    print (a + b)

def r_plus(a,b):
    return a + b 

p_result = p_plus(2,3)
r_result = r_plus(2,3)

print (p_result) # 5 None, return 을 받지 않으면 print는 컴퓨터의 입장에서는 그냥 아무것도 아니기에 None이다.
print (r_result) # 5

def r_plus(a, b):
    return a + b
    print ("osemthtin hrefealalalalalallala", True)

r_result = r_plus(2,4)
print (r_result) # 6
```

## 1.8 Keyworded Arguments
지금까지 사용한건 Positional Arguments(인자)라고 한다. -> 인자인데 위치에 의존하는 것이다.
하지만, 우리는 가끔 keyworkd argument를 가진다. 이게 뭐냐면? 인자인데 위치에 따라서 정해지는게 아닌 argument의
이름으로 쌍을 이뤄주는 것이다. 

```python
def plus(a,b):
    return a + b

result = plus(b = 30, a = 1)
print (result) # 31
```

* def를 정의할때는 name, age, are_from, fav_food 순서대로 작성을 해줘서 , keyworkd 별 arguments를 작성을 하지 않으면 헷갈린다.
* keywords arguments를 작성하면 age, name, fav_food, are_from 처럼 순서가 달라도 값을 미리 선정을 해주고 기존의 순서에 맞게 출력이 된다.
```python
def say_hello(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} your are from {are_from} you like {fav_food}" 

hello  = say_hello(age='12',name='nico', are_from='daegu', fav_food='pizza')
print (hello) # Hello nico you are 12 your are from daegu you like pizza
```

## 1.9 Code Challenge!
### 7가지 functions을 만드는 challenge
* plus
* minus
* times
* division
* negation
* power
* reminder
이 7가지의 함수가 포함되어있는 계산기를 만드는데, 유저가 함수를 호출할 때, 가끔 문자열을 쓴다면 이것의 예외처리도 해보자.

```python
class Calculator():
    def set_number(self, a, b):
        self.a = int(a)
        self.b = int(b)
    def plus(self):
        result = self.a + self.b
        return result
    
    def minus(self):
        result = self.a - self.b
        return result
    
    def times(self):
        result = self.a * self.b
        return result
    
    def division(self):
        result = self.a / self.b
        return result
    
    def negation(self):
        result = -self.a
        return result
    
    def power(self):
        result = self.a ** self.b
        return result
    
    def reminder(self):
        result = self.a % self.b
        return result
        
a = Calculator()
a.set_number(5, 10)
print (a.plus()) # 15
print (a.minus()) # -5 
print (a.times()) # 50
print (a.division()) # 0.5
print (a.negation()) # -5 
print (a.power()) # 9765625
print (a.reminder()) # 5
```

## 1.10 Conditionals part One
아래와 같은 에러를 해결하기 위해서는 지금은 if-else를 써본다?
```python
def plus(a,b):
   return a + b
   
plus(12, '10') # 이러한 문자열의 에러를 해결하기 위해서는??
```

```python
def plus(a,b):
    if (type(a) == str or type(b) == str):
        return "no string, use int"
    else: 
        return a + b

plus(12, '10') # no string, use int => 그런데, 이렇게 하면 다른 유형이 나오면 에러가 발생한다.

def b_plus(a,b):
    if type(a) is int or type(b) is float:
        return a + b
    else:
        return "Use type int"

print (b_plus(5, 10)) # 15
print (b_plus('5', 10)) # Use type lnt
```

## 1.11 if else and or -> conditions(조건문)
* Boolean Operations
    * or == x or y == if x is false, then y, eles x
    * and== x and y ==if x is false, then x, else y 
    * not== x not y ==if x is false, then True, else False

* 18세 미만이면 you can't drink 입력, age가 18 이거나 19살이면 you are new to this! , 20 살 초과하거나 25살 미만이면 your are still kind of young, 그 밖에는 enjoy your drink!

```python
# 18 세 이상면 음주 가능, 18세 이하면 음주 불가능
def age_check(age):
    print (f"you are {age}")
    if age < 18:
        print ("you can't drink")
    elif age == 18 or age == 19: 
        print ('you are new to this!')
    elif age > 20 and age < 25:
        print ('your are still kind of young')
    else:
        print ('enjoy your drink')

        
age_check(19) # your are 19 , your are new to this!
```

## 1.12 for in
'string, tuple 또는 list와 같이 배열의 요소를 순차적으로 가리킨다. 
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')

```python
for day in days:
    if day is 'Wed':
        break
    else:
        print(day, end=' ') # Mon Tue 

# string도 이론적으로는 배열이다.
for letter in 'nicolas':
   print (letter, end=' ') # n i c o l a s
```

## 1.13  Moduels
python에는 모듈들을 내장한다.
print 함수는 어떻게 무한적으로 인자를 받을 수 있을까? => 그 해답은 Django에??

* 기본적으로 모듈을 사용하는 방법
```python
import math
print (math.ceil(1.2)) # 1.2 올림하는 값
print (math.fabs(1.2)) # abs 
print (math.fabs(-1.2))
```

* 모듈에서 특정한 함수만을 가져오기
```python
from math import ceil, fsum

print (ceil(1.2))
print (fsum([1,2,3,4,5,6,7]))
```

* 모듈의 이름이 마음에 안들 때 내가 원하는 대로 바꾸기!
```python
from math import fsum as fm
```




















