print('Unesite vrijeme 1 (h min sec ):')
t1 = ((int(input('  h = '))) * 3600) + ((int(input('min = ')) * 60)) + ((int(input('sec = '))))

print('\n''Unesite vrijeme 2 (h min sec ):')
t2 = ((int(input('  h = '))) * 3600) + ((int(input('min = ')) * 60)) + ((int(input('sec = '))))

t3 = abs(t1 - t2)

hours = t3 // 3600
minutes = (t3 - hours * 3600) // 60
seconds = t3 % 60

print(f'\n''Izmedju ova dva trenutka je proteklo : \n'f'      {hours} h, 'f'{minutes} min, 'f'{seconds} sec')