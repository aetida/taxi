def sort_list():
    for i in range(number_empl-1):
        for j in range(number_empl-i-1):
            if taxi_price[j] < taxi_price[j+1]:
                taxi_price[j], taxi_price[j+1] = taxi_price[j+1], taxi_price[j]
                number_taxi[j], number_taxi[j+1] = number_taxi[j+1],number_taxi[j]
    print(' '.join(map(str, number_taxi)))
               
   
def sort_way():
    for i in range(number_empl-1):
        for j in range(number_empl-i-1):
            if way_dist[j] > way_dist[j+1]:
                 way_dist[j], way_dist[j+1] = way_dist[j+1], way_dist[j]           


number_empl = int(input('Введите количество сотрудников: '))
way_dist = []
taxi_price = []
number_taxi = []
count_1 = 0
count_2 = 0
final_price = 0

while count_1 < number_empl:
    print('Введите расстояние для сотрудника №', count_1 + 1,':', end=' ')
    way_dist.append(int(input()))
    count_1 += 1

while count_2 < number_empl:
    print('Введите тариф такси №', count_2 + 1, ':', end=' ')
    taxi_price.append(int(input()))
    number_taxi.append(count_2+1)
    count_2 += 1


sort_list()
sort_way()


for i in range(number_empl):
    final_price += way_dist[i]*taxi_price[i]

print('Общая стоимость: ', final_price)

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

hundred = ['сто ','двести ','триста ', 'четыреста ','пятьсот ','шестьсот ','семьсот ','восемьсот ','девятьсот ']
dozens = ['десять ','одиннадцать ','двенадцать ','тринадцать ','четырнадцать ','пятнадцать ','шестнадцать ','семнадцать ','восемнадцать ','девятнадцать ', 'двадцать ','тридцать ','сорок ','пятьдесят ','шестдесят ','семдесят ','восемдесят ','девяносто ',''] 
thousands = ['','тысяча ', 'тысячи ','тысяч ']
unit = ['один ','два ','три ','четыре ','пять ','шесть ','семь ','восемь ','девять ','одна ','две ']
rubl = ['рубль','рубля','рублей']

if x != 0:
	s = hundred[x-1]
else:
	s = thousands[0]

if z != 0:
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
else:
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

if x!=0 or z!=0 or c!=0:
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

if v != 0:
	g = hundred[v-1]
else:
	g = thousands[0]

if b != 0:
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
else:
	h = thousands[0]
	if n != 0:
		j = unit[n-1]
	else:
		j=thousands[0]

if n == 1:
	if b!=1:
		r=rubl[0]
	else:
		r=rubl[2]
else:
	pass

if n == 2 or n == 3 or n ==4:
	if b!=1:
		r=rubl[1]
	else:
		r = rubl[2]
else:
	pass

if n > 4 or n == 0:
	r = rubl[2]
else:
	pass

print(str(s)+str(d)+str(f)+str(m)+str(g)+str(h)+str(j)+str(r))