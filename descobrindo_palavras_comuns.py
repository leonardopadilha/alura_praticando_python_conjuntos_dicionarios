
texto1 = set(input("texto 1: ").lower().split())
texto2 = set(input("texto 2: ").lower().split())


palavras_comuns = texto1.intersection(texto2)
print(texto1.intersection(palavras_comuns))