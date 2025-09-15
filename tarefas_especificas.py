equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

tarefas_combinadas = equipe_a.union(equipe_b)

tarefa_removida = input("Digite a tarefa a ser removida: ").strip().lower()

if tarefa_removida in tarefas_combinadas:
  tarefas_combinadas.remove(tarefa_removida)

print(f"Tarefas combinadas: {tarefas_combinadas}")