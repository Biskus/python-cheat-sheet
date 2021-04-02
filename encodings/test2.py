



words = [
    'hei',
    'hå',
    'æ',
    'ø',
    'å'
]
print(words)



for w in words:
    print(f'{w}: {w.encode()}')

print(b'\xc3\xa6'.decode('utf-8'))