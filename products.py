
products = []

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價格:')
	#p = []
	#p.append(name)
	#p.append(price)

	products.append([name,price])
print(products)

#print(products[0][0])
#print(products[1][0])