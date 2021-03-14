import math

#string formatting
fruits = [
    'Banana',
    'Apple'
]



for f in fruits:
    pre = 'Hello I like '
    
    print(pre + f'{f}')
    print(pre + '%s' % f)



amount = 1.50482784329856723489504327689
pi = math.pi
amount = pi
print('I have %d liters' % amount)
print('I have {:0.10} liters'.format(amount))

fagkoder = [
    '2ik1',
    '2ik2',
]

for f in fagkoder:
    print(f'Jeg går {f.upper()}-linjen')

