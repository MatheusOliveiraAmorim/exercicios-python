somaCartas = int(input("Digite a soma das suas cartas: "))

if somaCartas <= 10:
    print("Sem dúvida compre mais uma carta")
elif somaCartas > 10 and somaCartas <= 15:
    print("Há um risco, mas aconselho a comprar mais uma carta")
elif somaCartas > 15 and somaCartas <= 20:
    print("Aconselho a parar de jogar")
elif somaCartas == 21:
    print("Você já venceu, não precisa comprar mais nada")
else:
    print("Você perdeu")