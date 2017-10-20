areapintada = int(input('Digite a área a ser pintada:'))
litros = areapintada/6
latasG = litros/18
if litros/18 != litros//18:
    latasG = (litros//18) + 1
latasP = litros/3.6
if latasP != litros//3.6:
    latasP = (litros//3.6) + 1
precoG = latasG*80
precoP = latasP*25
print('Com latas de 18 litros: %d reais e %d latas' %(precoG, latasG))
print('Com latas de 3.6 litros: %d reias e %d latas' %(precoP, latasP))
latasM = 0
if (litros/18) - (litros//18) > 1/5 and (litros/18) - (litros//18) <= 2/5:
    latasM += 2
    latasG -= 1
elif (litros/18) - (litros//18) > 2/5 and (litros/18) - (litros//18) <= 3/5:
    latasM += 3
    latasG -= 1
elif (litros/18) - (litros//18) > 3/5 and (litros/18) - (litros//18) <= 4/5:
    latasM += 4
    latasG -= 1
elif (litros/18) - (litros//18) > 4/5 and (litros/18) - (litros//18) < 1:
    lstasM += 5
    latasG -= 1
print('Usando os dois tipos de latas: %d latas grandes e %d latas pequenas, no valor de %d' %(latasG, latasM, ((latasG*80)+(latasM*25))))
