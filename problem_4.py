# '''Вы работаете в Банке и пишите программу которая считает % для кредита.
#  Спросите у пользователя сумму займа(не меньше 50 000) 
#  и посчитайте сколько нужно будет вернуть если % = 3.47, 
#  результат округлите до 2 чисел после точки. 

# Формула подсчёта переплаты: Сумма * (% / 100)'''

# while True:
# 	if input('Вы хотите взять займ у банка? Y/n').lower() in 'y':
# 		
print('Вы хотите взять займ у банка')
pay = float(input('Введите размер кредита ( > 50 000) -> '))
cred_proc = 3.47
ret_pay = pay * (1 + cred_proc/100)
print('Нужно вернуть {:.2f}'.format(round(ret_pay, 2)))