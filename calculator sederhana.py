'''Program kalkulator sederhana'''
#fungsi penjumlahan
def add(x,y):
    return x + y

#fungsi pengurangan
def subtract(x,y):
    return x - y

#fungsi perkalian
def multiply(x,y):
    return x * y

#fungsi pembagian
def devide(x,y):
    return x / y

#menu oprasi
print ('Pilih oprasi yang ingin di gunakan :')
print ('1. Penjumlahan')
print ('2. Pengurangan')
print ('3. Perkalian')
print ('4. Pembagian')

#meminta input user
choice = input ('masukkan pilihan : ')

num1 = int(input('Masukkan bilangan pertama : '))
num2 = int(input('Masukkan bilangan kedua   : '))

if choice == '1':
    print (num1,'+',num2,'=',
add(num1,num2))
elif choice == '2':
    print (num1,'-',num2,'=',
add(num1,num2))
elif choice == '3':
    print (num1,'x',num2,'=',
add(num1,num2))
elif choice == '4':
    print (num1,'/',num2,'=',
add(num1,num2))
else:
    print('maaf,oprasi bilangan tidak tersedia')

