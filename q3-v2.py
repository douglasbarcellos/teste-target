import json

# Lê o arquivo JSON com os valores de faturamento diário
with open('dados.json', 'r') as file:
    faturamento = json.load(file)

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")

# Calcula a média mensal, ignorando dias sem faturamento
dias_com_faturamento = [f for f in faturamento if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
print(f"Média mensal: {media_mensal}")

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = len([f for f in dias_com_faturamento if f > media_mensal])
print(f"Dias acima da média mensal: {dias_acima_da_media}")
