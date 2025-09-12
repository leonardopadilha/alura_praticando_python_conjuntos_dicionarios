participantes = {
  "Workshop 1": { "Alice", "Bruno", "Carla", "Diego" },
  "Workshop 2": { "Fernanda", "Gustavo", "Helena" }
}

print(f"Nomes dos participantes do Workshop 1: {', '.join(participantes['Workshop 1'])}")
print(f"Nomes dos participantes do Workshop 2: {', '.join(participantes['Workshop 2'])}")

nome_removido = input("Nome do participante a ser removido: ")


for workshop, participante in participantes.items():
  if nome_removido in participante:
    participante.remove(nome_removido)
    print(f"Participante {nome_removido} removido do Workshop {workshop}")


"""
for workshop, nomes in participantes.items():
  nomes.discard(nome_removido)
"""

print("Lista atualizada de participantes:")
for workshop, nome in participantes.items():
  print(f"{workshop}: { nome }")