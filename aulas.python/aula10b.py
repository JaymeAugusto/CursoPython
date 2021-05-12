n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
# Jeito horrivel de fazer essa merda
# print('Sua media foi boa! PARABENS!'if m>=6 else 'Sua media foi ruim! ESTUDE MAIS!')
if m >=6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')