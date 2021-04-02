# encoding: utf-8

outfile = 'test4.txt'

alfabetet = 'abcdefghijklmnopqrstuvwxizæøå'

with open(outfile,'w', encoding='utf-8') as f1:
    f1.write(alfabetet)

with open(outfile, encoding='utf-8') as f2:
    print(f2.read())

with open(outfile, 'rb') as f3:
    print(f3.read())

print(f1.encoding)
print(f2.encoding)