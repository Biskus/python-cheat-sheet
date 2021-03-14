from pprint import pprint as print
from math import pi


vars = {
    'name' : 'Arvid',
    'age': 19,
    'occupation':'Programmer',
}

string = 'Hi my name is %s, Im %s years old and work as a %s'
print(string % tuple((vars.values())))

string = f'Hi my name is {vars["name"]}, Im {vars["age"]} years old and work as a {vars["occupation"]}'
print(string)

string = 'Hi my name is {}, Im {} years old and work as a {}'
print(string.format(vars['name'],vars['age'],vars['occupation']))

"""
https://mkaz.blog/code/python-string-format-cookbook/
"""

print (pi) #3.141592653589793
print (type(pi)) #float
print (f'{pi:.0f}') #3
print (f'{pi:.2f}') #3.14
print (f'{pi:.3f}') #3.142
print (f'{pi:.6f}') #3.141593
print (f'{pi:.25f}') #3.1415926535897931159979635
print (f'{pi:.30f}') #3.141592653589793115997963468544
print (f'{pi:.48f}') #3.141592653589793115997963468544185161590576171875
print (f'{pi:.99f}') #3.141592653589793115997963468544185161590576171875000000000000000000000000000000000000000000000000000


print(f'Hello the value of pi with 2 decimals is: {pi:.2f}')
print(f'Hello the value of pi with 10 decimals is: {pi:.10f}')