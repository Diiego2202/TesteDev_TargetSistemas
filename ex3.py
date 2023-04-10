import json

with open('dados.json', 'r') as d:
    dados = json.load(d)

faturamento_diario = [dia['valor'] for dia in dados]

min_faturamento = min(faturamento_diario)
max_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

acima_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

print("Menor valor: R$", min_faturamento)
print("Maior valor: R$", max_faturamento)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", acima_media)
