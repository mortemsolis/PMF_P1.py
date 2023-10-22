from math import pi

pr = float(input('Unesite broj između 1 i 4: '))
if pr == 1:
    r = float(input('Unesite realan broj (poluprečnik kruga): '))
    print(f'Površina je {r*r*pi:.2f}, a obim je {2*r*pi:.2f}')
elif pr == 2:
    a = int(input('Unesite jedan prirodan broj (stranica "a" pravougaonika): '))
    b = int(input('Unesite drugi prirodan broj (stranica "b" pravougaonika): '))
    print(f'Površina je {a*b}, a obim je {(a*2)+(b*2)}')
elif pr == 3:
    a = float(input('Unesite pozitivan realan broj (stranica kvadrata): '))
    if a > 0:
        print(f'Površina kvadrata iznosi {a*a:.2f}')
    else:
        print('Broj nije pozitivan!')
elif pr == 4:
    a = float(input('Unesite jedan cijeli broj "a" : '))
    b = float(input('Unesite drugi cijeli broj "b" : '))
    if a > b:
        print('Broj "a" je veći od "b".')
    elif b > a:
        print('Broj "b" je veći od "a".')
    else:
        print('Brojevi su jednaki.')
else:print('Slušaš li ti mene?')
