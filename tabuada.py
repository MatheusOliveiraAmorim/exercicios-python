multiplicando = 2
multiplicador = 0
while multiplicador < 10 and multiplicando <= 9:
    multiplicador += 1
    produto = multiplicando * multiplicador
    print(multiplicando, "x", multiplicador, "=", produto)
    if multiplicador == 10:
        print("\t")
        multiplicador = 0
        multiplicando += 1