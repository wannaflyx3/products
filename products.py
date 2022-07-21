import os #operating system，載入作業系統

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續，跳到下一次迴圈
			name, price = line.strip().split(',')  #先進行strip() :捨棄換行符號\n，再進行split(','):逗號分隔
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	
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
	return products

	#print(products[0][0])
	#print(products[1][0])

#印出所有購買紀錄
def print_products(products):
	
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')  #一定要有換行符號「\n」



def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在電腦裡
		print('yeah! 找到檔案')
		products = read_file(filename)
	else:
		print('找不到檔案.....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()