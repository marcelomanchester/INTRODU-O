area = int(input('digite o tamanho da área a ser pintada:'))
Qntlitros = area/3
print(Qntlitros)
Qntlatas = Qntlitros/18
print(Qntlatas)
if (Qntlatas/18)%1 != 0:
    Qntlatas = (Qntlitros//18) + 1
print('Serão necessárias %d latas no valor de %d'%(Qntlatas,(Qntlatas*80)))
