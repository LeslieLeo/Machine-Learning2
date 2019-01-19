print('''这是一段多行字符串。这是它的第一行
This is the second line.
"What's your name?," I asked
He said "Bond, James Bond."
''')






age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

print(name + 'is' + str(age) + 'years old')

#对于浮点数‘0.333’保留小数点（.）后三位
print('{0:.3f}'.format(1.000/3))

#使用下划线填充文本，并保持文字处于中间位置
#使用（^）定义‘___hello___’字符串长度为11
print('{0:_^9}'.format('hello'))
#基于关键词输出...
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end=' ')
print('b', end=' ')
print('c')

#用反斜杠来制定单引号
print('What\'s your name')
#换行\n 制表\t
print('This is the first line\nThis is the second line')
print('This is the first line\tThis is the second line')

#在一个字符串中，一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行。
print("This is the first sentence.\
      This is the second sentence")

r"Newlines are indicated by \n"
print('This is the first line\nThis is the second line')
