multiplicando = 2
multiplicador = 0
for multiplicando in range (2,10):
    for multiplicador in range(0,10):
        multiplicador += 1
        produto = multiplicando * multiplicador
        print(multiplicando, "x", multiplicador, "=", produto)
    print("")
    multiplicando += 1