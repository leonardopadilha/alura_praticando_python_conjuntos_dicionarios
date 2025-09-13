estoque = {
  "Caderno universitário": 50,
  "Caneta azul": 120,
  "Borracha branca": 30
}

produto_atualizado = input("Nome do produto a ser atualizado: ")
quantidade_atualizada = int(input("Nova quantidade: "))

for produto in estoque.keys():
  if produto == produto_atualizado:
    estoque[produto] = quantidade_atualizada

print(estoque)