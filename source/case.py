import json 

with open("source/exemplos.json", "r", encoding="utf-8") as arquivo:
    data_json = json.load(arquivo)

i = 0
for cliente in data_json:
    print(f"CLIENTE {i}:")
    print(cliente["perfil"], cliente["score_max_risco"], cliente["carteira"][0]["risco"])
    for cart_infos in cliente["carteira"]:
        print(cart_infos["ativo"], cart_infos["risco"], cart_infos["valor_investido"])
    print(cliente["nova_ordem"])
    print("\n")
    i += 1

# Cálculo do Risco Atual da Carteira:
risco_atual = 0
for cliente in data_json:
    numeradores_parciais = []
    denominadores_parciais = []
    print(f"CLIENTE {i}:")
    for cart_infos in cliente["carteira"]:
        numeradores_parciais.append(cart_infos["risco"] * cart_infos["valor_investido"])
        denominadores_parciais.append(cart_infos["valor_investido"])
    print(round((sum(numeradores_parciais)) / (sum(denominadores_parciais)), 2))
    print("\n")
    i += 1
