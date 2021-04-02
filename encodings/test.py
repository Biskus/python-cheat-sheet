# encoding: utf-8

most_used_encodings = [
    'cp1252',
    'latin1',
    'utf-8',
    'ascii'
]

filename = 'text.txt'

with open(filename,) as file:
    text = file.read()
    print(file.encoding)

print(text)

with open(filename, 'rb') as file:
    text = file.read()
print(text)
print(text.decode('utf-8'))