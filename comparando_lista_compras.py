laura = set(input("Lista de Laura: ").split(", "))
ana = set(input("Lista de Ana: ").split(", "))

itens_comuns = laura.intersection(ana)
itens_exclusivos_laura = laura.difference(ana)
itens_exclusivos_ana = ana.difference(laura)

print(f"""
Itens em ambas as listas: {', '.join(itens_comuns)}
Itens exclusivos de Laura: {', '.join(itens_exclusivos_laura)}
Itens exclusivos de Ana: {', '.join(itens_exclusivos_ana)}
""")