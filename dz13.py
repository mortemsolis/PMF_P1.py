from math import pi, acos

a = float(input())
b = float(input())
c = float(input())

if acos(((b**2 + c**2 - a**2) / (2*b*c))) == pi / 2:
    print('Trougao je pravougli.')
elif acos(((a**2 + c**2 - b**2) / (2*a*c))) == pi / 2:
    print('Trougao je pravougli.')
elif acos(((a**2 + b**2 - c**2) / (2*a*b))) == pi / 2:
    print('Trougao je pravougli.')
else:
    print('Trougao nije pravougli.')
    