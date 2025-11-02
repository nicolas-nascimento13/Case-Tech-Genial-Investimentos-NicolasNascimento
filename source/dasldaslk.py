import json

saida = {
    "status": "Aprovado",
    "risco_projetado": 2.1,
    "mensagem": "Ordem executada. Carteira em conformidade."
}
with open(r"source/relatorio_case.json", "w") as f:
    json.dump(saida, f, indent = 4)