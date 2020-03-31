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













