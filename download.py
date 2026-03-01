import requests
import os
import json

# Lê a lista de provas
with open("provas.json", "r") as f:
    provas = json.load(f)

print(f"📋 {len(provas)} arquivos encontrados na lista\n")

# Baixa cada uma
for prova in provas:
    # Monta o caminho da pasta automaticamente
    pasta = f"data/{prova['instituicao']}/{prova['ano']}/{prova['tipo']}"
    os.makedirs(pasta, exist_ok=True)

    # Nome do arquivo
    arquivo = f"{pasta}/{prova['nome']}.pdf"

    # Pula se já foi baixado
    if os.path.exists(arquivo):
        print(f"⏭️  Já existe: {arquivo}")
        continue

    # Faz o download
    print(f"⬇️  Baixando {prova['instituicao'].upper()} {prova['ano']} — {prova['tipo']}...")
    response = requests.get(prova['url'])

    # Salva o arquivo
    with open(arquivo, "wb") as f:
        f.write(response.content)

    print(f"✅ Salvo em {arquivo}\n")

print("🎉 Todos os downloads concluídos!")