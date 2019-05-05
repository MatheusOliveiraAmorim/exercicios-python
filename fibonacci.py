numero = int(input("Digite o termo desejado: "))
ultimo = 1
penultimo = 1
if (numero == 1) or (numero == 2):
    print("1")
else:
    for count in range(2, numero):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)