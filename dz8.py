import math

a = ((float(input('a= '))*math.pi)/180)
n = float(input('n= '))
k = float(input('k= '))
h = float(input('h= '))
print('-----------------------')
print(f'Rezultat je: {(2*(k**(2/3)))/(math.sin(a)*math.sqrt(h+n))*math.cos(a):.2f}')