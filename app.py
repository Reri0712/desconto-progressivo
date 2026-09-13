# Programa de Desconto Progressivo - Loja Online
# Autor: Renato

# Entrada de dados
valor_total = float(input("Digite o valor total da compra (R$): "))

# Regras de desconto
if valor_total < 200.00:
    percentual_desconto = 0.05
elif valor_total < 300.00:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

# Cálculos
valor_desconto = valor_total * percentual_desconto
valor_final = valor_total - valor_desconto

# Exibição do resultado
print("\n--- Resumo da Compra ---")
print(f"Valor original da compra: R$ {valor_total:.2f}")
print(f"Desconto aplicado ({int(percentual_desconto * 100)}%): R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")