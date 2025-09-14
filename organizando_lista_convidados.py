convidados = set()

while True:
  nome_convidado = input("Digite o nome do convidado ou 'sair' para encerrar: ")
  if nome_convidado.lower() == "sair":
    break
  convidados.add(nome_convidado)


print(f"Convidados confirmados: {', '.join(convidados)}")