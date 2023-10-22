stanje = 8550
pozdrav = 'Hvala na korištenju, doviđenja!'

password = int(input('Pozdrav, uneste šifru: '))
if password < 1000 or password >= 10000:
    print('\nNije pravilna šifra!')
else:
    print('''\nDobrodošli, odaberite opciju:
    1. Pregled stanja
    2. Uplata
    3. Isplata
    4. Izlaz''')
    opt = input()
    if opt == '1':
        print(f'\nStanje na računu iznosi {float(stanje):,.2f} KM\n{pozdrav}')
    elif opt == '2':
        uplata = int(input('\nUnesite količinu za uplatu: '))
        if uplata <= 0:
            print('Nemoguće uplatiti manje od KM1.00')
        elif uplata > 2000:
            print('Nemoguće uplatiti više od KM2,000.00')
        else:
            stanje = stanje + uplata
            yesno = input('\nUplata uspješna!\nŽelite li prikaz konačnog stanja?\n\n(D ili N)... ')
            if yesno == 'd' or yesno == 'D':
                print(f'\nStanje na računu iznosi {float(stanje):,.2f} KM\n{pozdrav}')
            elif yesno == 'n' or yesno == 'N':
                print(f'\n{pozdrav}')
            else:
                print('\nPogrešan unos!')
    elif opt == '3':
        isplata = int(input('\nUnesite količinu za isplatu: '))
        if isplata <= (stanje + 500) and isplata > 0 and (isplata % 100) == 0:
            stanje = stanje - isplata
            print(f'\nStanje na računu iznosi {float(stanje):,.2f} KM\n{pozdrav}')
        else:
            print('\nPogrešan unos!')
    elif opt == '4':
        print(f'\n{pozdrav}')
    else:
        print('\nPogrešan unos!')
        