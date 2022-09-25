print("--- Sonho do funcionário ---")

salário = float(input("Digite o salário atual: R$"))
aumento = (salário / 100 * 15)
novoSalário = salário + aumento
print(f"De R${salário}, você receberá um aumento de R${aumento:.2f}, totalizando em R${novoSalário:.2f}")
