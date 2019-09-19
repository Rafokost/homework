import datetime
print(datetime.date.today())

U=input('U is inner energy = ')
U=int(U)
print(U<10 and U!=5)

P=input('P is gas pressure = ')
P=int(P)
print(P<=10 or U!=-9)

V=input('V is volume of gas = ')
V=int(V)
print(V==8 and V!=9 or V<3)

print('H=U+P*V')
H=U+P*V
H=str(H)
print('the value of H is',H)
H=int(H)

print(bool(H) and H>=0)

