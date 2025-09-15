permissoes_principais = set(input("Permissões principais: ").strip().lower().split(", "))
permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(", "))

eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

if eh_subconjunto:
  print("As permissões solicitadas fazem parte das permissões principais.")
else:
  print("As permissões solicitadas não fazem parte das permissões principais.")