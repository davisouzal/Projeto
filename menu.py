print("""MENU
1 - Gerar chave Pública
2 - Encriptar
3 - Desencriptar""")
opcao = int(input("Digite aqui sua opção: "))
if(opcao>=1 and opcao<=3):
    if(opcao==1):
        p = int(input("Digite aqui o valor de p: "))
        q = int(input("Digite aqui o valor de q: "))
else:
    print("Por favor digite uma opção válida")
