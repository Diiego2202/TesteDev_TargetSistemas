fat_sp = 67836.43
fat_rj = 36678.66
fat_mg = 29229.88
fat_es = 27165.48
fat_outros = 19849.53

valor_total_mensal = fat_sp + fat_rj + fat_mg + fat_es + fat_outros

percentual_sp = (fat_sp / valor_total_mensal) * 100
percentual_rj = (fat_rj / valor_total_mensal) * 100
percentual_mg = (fat_mg / valor_total_mensal) * 100
percentual_es = (fat_es / valor_total_mensal) * 100
percentual_outros = (fat_outros / valor_total_mensal) * 100

print("Percentual de representação que cada estado teve dentro do valor total mensal da distribuidora:")
print("SP: {:.2f}%".format(percentual_sp))
print("RJ: {:.2f}%".format(percentual_rj))
print("MG: {:.2f}%".format(percentual_mg))
print("ES: {:.2f}%".format(percentual_es))
print("Outros: {:.2f}%".format(percentual_outros))
