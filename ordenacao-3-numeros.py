a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, a, c)
elif c < a < b:
    print(c, a, b)
elif c < b < a:
    print(c, b, a)