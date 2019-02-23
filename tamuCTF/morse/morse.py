f = open('flag.txt', 'r')

code = f.readline()
print(code)

code = code.replace('dah', '_')
code = code.replace('dit', '. ')
code = code.replace('di', '.')
# code = code.replace(' ', '/')
code = code.replace('-', '')

print(code)
