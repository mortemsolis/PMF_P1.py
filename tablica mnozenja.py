a = 0
while (a<10000):
    a = a+1
    b = 0
    #print('\n','-'*158)
    print('\n')
    while (b<10000):
        b= b+1
        print(f'{a:>2} * {b:<2} = {a*b:<3}', end=' | ')