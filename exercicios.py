
try:
    quantidade = float(input("Digite a quantidade : "))
    preco = float(input("Digite o preço : "))
    if quantidade > 0 and preco > 0:
        print("Dados válidos")
    else : print("Dados inválidos")
except ValueError: print("ERRO XXXXXX, Digite números")     
