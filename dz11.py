br = int(input('Unesite petocifren broj: '))
br = abs(br)

if br < 10000 and br >= 100000:
    print('Broj nije petocifren!')
else:
    a = br // 10000
    b = (br % 10000) // 1000
    c = (br % 1000) // 100
    d = (br % 100) // 10
    e = br % 10
    
    if a == e and b == d:
        print(f'Broj {br} je palindrom.')
    else:
        print(f'Broj {br} nije palindrom.')