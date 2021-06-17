'''Возьмите код #1 с Classroom и создайте для него try... except...
 Создайте несколько except выражений для разных типов ошибок.'''

at = 10
a = 15
wo = 20
try:
    for e in range(-at, at):
    print(wo / e)
    if at > '5':
    print("at > 5")
except SyntaxError:
	print('Синтаксическая ошибка')
except IndentationError	:
	print("oshibka")
else:
	print('net oshibok')
finally:    
	print('v lubom sluchae')