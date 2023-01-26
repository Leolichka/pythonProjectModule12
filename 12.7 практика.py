per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Ведите сумму, которую планируете положить под процент: "))

per_cent_val = list(per_cent.values())
TKB = int(per_cent_val[0]*money/100)
CKB = int(per_cent_val[1]*money/100)
VTB = int(per_cent_val[2]*money/100)
SBER = int(per_cent_val[3]*money/100)
deposit = [TKB, CKB, VTB, SBER]

print('Накопленные средства за год вклада в каждом из банков: ', '\n', 'ТКБ-',TKB, '\n', 'СКБ - ', CKB, '\n', 'ВТБ - ', VTB, '\n', 'СБЕР - ', SBER)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))