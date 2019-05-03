horaTrabalhada = int(input("Quantidade de horas trabalhadas: "))
valorHora = int(input("Valor da hora trabalhada: "))
percentualDesconto = int(input("Percentual de desconto: "))


salarioBruto = horaTrabalhada * valorHora

totalDesconto = (percentualDesconto*salarioBruto)/100

salarioLiquido = salarioBruto - percentualDesconto

print("Salário bruto:", salarioBruto,
      "Total a ser descontado:", totalDesconto,
      "Salário líquido:", salarioLiquido)