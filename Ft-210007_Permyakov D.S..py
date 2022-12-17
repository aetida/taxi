def sort_list(): #сортировка пузырьком тарифов и номеров такси
    for i in range(number_empl-1):
        for j in range(number_empl-i-1):
            if taxi_price[j] < taxi_price[j+1]:
                taxi_price[j], taxi_price[j+1] = taxi_price[j+1], taxi_price[j]
                number_taxi[j], number_taxi[j+1] = number_taxi[j+1],number_taxi[j]
    print(' '.join(map(str, number_taxi))) #вывод строки ответа
               
   
def sort_way(): #сортировка пузырьком расстояний
    for i in range(number_empl-1):
        for j in range(number_empl-i-1):
            if way_dist[j] > way_dist[j+1]:
                 way_dist[j], way_dist[j+1] = way_dist[j+1], way_dist[j]           

#обработка ввода количества сотрудников
while True:
	try:
		number_empl = int(input('Введите количество сотрудников (от 1 до 1000): '))
		if number_empl <1 or number_empl >1000:
			print('некорректный ввод\nповторите попытку')
		else:
			break
	except ValueError:
		print('некорректный ввод\nповторите попытку')
			
way_dist = [] #создание переменных для расстояний, тарифов
taxi_price = []
number_taxi = [i+1 for i in range(number_empl)] #заполнение списка номеров такси
final_price = 0 #переменная для окончательной цены			


for i in range(number_empl): # цикл обработки ввода расстояний
    while True:
        string=input(f'Расстояние до дома {i+1} сотрудника: ')
        try:
            way_dist.append(int(string))
            break
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')


for i in range(number_empl): #цикл обработки ввода тарифов такси
    while True: 
        string = input(f'Тариф {i+1} такси: ')

        try:
            taxi_price.append(int(string))
            break
        except ValueError:
            print ('некорректный ввод\nповторите попытку')

#обращение к функциям сортировки списков
sort_list()
sort_way()


for i in range(number_empl): #цикл расчета итоговой цены
    final_price += way_dist[i]*taxi_price[i]

print('Общая стоимость: ', final_price) #цикл расчета итоговой цены

#алгоритм перевода числа в буквенную запись
#разбиение числа на разряды
x = final_price//100000
final_price = final_price - x*100000
z = final_price//10000
final_price = final_price - z*10000
c = final_price//1000
final_price = final_price - c*1000
v = final_price//100
final_price = final_price - v*100
b = final_price//10
final_price = final_price - b*10
n = final_price//1 

#создание списков с буквенной записью
hundred = ['сто ','двести ','триста ', 'четыреста ','пятьсот ','шестьсот ','семьсот ','восемьсот ','девятьсот ']
dozens = ['десять ','одиннадцать ','двенадцать ','тринадцать ','четырнадцать ','пятнадцать ','шестнадцать ','семнадцать ','восемнадцать ','девятнадцать ', 'двадцать ','тридцать ','сорок ','пятьдесят ','шестдесят ','семдесят ','восемдесят ','девяносто ',''] 
thousands = ['','тысяча ', 'тысячи ','тысяч ']
unit = ['один ','два ','три ','четыре ','пять ','шесть ','семь ','восемь ','девять ','одна ','две ']
rubl = ['рубль','рубля','рублей']

if x != 0: # обработка разряда сотен тысяч
	s = hundred[x-1]
else:
	s = thousands[0]

if z != 0: # обработка разряда десятков тысяч и тысяч если первое не равно 0
	if z == 1:
		if c == 0:
			d = dozens[0]
			f = thousands[0]
		else:
			d = dozens[c]
			f = thousands[0]
	else:
		d = dozens[z+8]
		if c != 0:
			f = unit[c-1]
		else:
			f=thousands[0]
else: # обработка разряда тысяч если десятки тысяч равны 0
	d = thousands[0]
	if c != 0:
		if c == 1:
			f=unit[9]
		else:
			f = unit[c-1]
		if c == 2:
			f=unit[10]
	else:
		f=thousands[0]

if x!=0 or z!=0 or c!=0: #склонение слова "тысяча"
	if z == 1 or (c!=2 and c!=3 and c!=4 ):
		m = thousands[3]
	else:
		pass
	if z!=1 and c ==1:
		m=thousands[1]
	else:
		pass
	if z!=1 and (c==2 or c==3 or c==4):
		m=thousands[2]
	else:
		pass
	if x!=0 and z==0 and c==0:
		m=thousands[3]
	else:
		pass
	if x!=0 and c ==0:
		m=thousands[3]
	else:
		pass
else:
	m=thousands[0]

if v != 0: # обработка разряда сотен
	g = hundred[v-1]
else:
	g = thousands[0]

if b != 0: # обработка разряда десятков и единиц если перве не равно 0
	if b == 1:
		if n == 0:
			h = dozens[0]
			j = thousands[0]
		else:
			h = dozens[n]
			j = thousands[0]
	else:
		h = dozens[b+8]
		if n != 0:
			j = unit[n-1]
		else:
			j=thousands[0]
else: # обработка разряда единиц если десятки равны 0
	h = thousands[0]
	if n != 0:
		j = unit[n-1]
	else:
		j=thousands[0]

if n == 1: # склонение рублей если число оканчивается на 1
	if b!=1:
		r=rubl[0]
	else:
		r=rubl[2]
else:
	pass

if n == 2 or n == 3 or n ==4:  # склонение рублей если число оканчивается на 2 3 4
	if b!=1:
		r=rubl[1]
	else:
		r = rubl[2]
else:
	pass

if n > 4 or n == 0: # склонение рублей при остальных случаях окончания
	r = rubl[2]
else:
	pass

print(str(s)+str(d)+str(f)+str(m)+str(g)+str(h)+str(j)+str(r)) # вывод числа словами
