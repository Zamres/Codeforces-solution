n = int(input())
hate = True
while n != 0:
    n -= 1
    if hate:
        print('I hate', end=' ')
        hate = False
    else:
        print('I love', end=' ')
        hate = True
    if n != 0:
        print('that', end=' ')
print('it')
