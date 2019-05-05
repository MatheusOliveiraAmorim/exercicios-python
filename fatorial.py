fatorial = int(input("Digite o numero para fatorar: "))
resultado = 1
for n in range(1, fatorial + 1):
    resultado *= n
print(resultado)