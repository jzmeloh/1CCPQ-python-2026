def varificacao_de_nota(nota):
    while nota < 0 or nota > 10:
        print("a nota digitada eh invalida")
        nota = float(input("digite a nota novamente"))


nota_A = float (input("digite a primeira nota nota : "))


while nota_A < 0 or nota_A > 10:
    print("a nota digitada eh invalida")
    nota_A = float(input("digite a nota novamente"))
nota_B = float (input("digite a primeira nota nota : "))
while nota_B < 0 or nota_B > 10:
    print("a nota digitada eh invalida:")
    nota_B = float(input("digite a nota novamente:"))
media = (nota_A + nota_B) / 2
print(media)
