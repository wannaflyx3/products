#讀取檔案

products = []

with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續，跳到下一次迴圈
		name, price = line.strip().split(',')  #先進行strip() :捨棄換行符號\n，再進行split(',')
		products.append([name, price])
print(products)







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

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  #一定要有換行符號「\n」
