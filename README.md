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
## Tuples and Dicts -> Immutable sequence











