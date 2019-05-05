f = int(input("Digite o valor final: "))
nAnt = 0
for n in range(1, f+1, 1):
    nAnt = n + nAnt
    print(n)
print("Total: ", nAnt)