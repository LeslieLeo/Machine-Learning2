number = 23
guess = int(input('Enter an integer :'))

if guess == number:#在结尾处包含一个冒号,我们借此向 Python 指定接下来会有一块语句在后头
    #新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you du not win any prizes!)')
    #新块在这里结束
elif guess < number:
    #另一代码块
    print('No, it is a little higher than that')
    #你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No, it is a little lower than that')
    #你必须通过猜测一个大于（>）设置数的数字来到达这里

print('Done')
#这最后一句语句将在
#if语句执行完毕后执行
