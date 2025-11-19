import requests
import threading
import asyncio
from collections import Counter, defaultdict, deque
from itertools import combinations

# -------------------------------------------------
# 1. Baixar dados da API com threads
# -------------------------------------------------
URLS = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 11)]
resultados = deque()  # fila para guardar resultados

def baixar(url):
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            resultados.append(resp.json())
    except Exception as e:
        print(f"Erro em {url}: {e}")

threads = [threading.Thread(target=baixar, args=(url,)) for url in URLS]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"[INFO] Dados coletados: {len(resultados)} posts")

# -------------------------------------------------
# 2. Processamento com collections + itertools
# -------------------------------------------------
# Contar palavras mais comuns nos títulos
titulos = [item["title"] for item in resultados]
todas_palavras = " ".join(titulos).split()
contagem = Counter(todas_palavras)

print("\nPalavras mais comuns:")
for palavra, freq in contagem.most_common(5):
    print(f"{palavra}: {freq}x")

# Agrupar posts por userId usando defaultdict
grupos = defaultdict(list)
for item in resultados:
    grupos[item["userId"]].append(item["title"])

print("\nPosts por usuário:")
for user, posts in grupos.items():
    print(f"Usuário {user}: {len(posts)} posts")

# Ver combinações de 2 palavras que aparecem nos títulos
print("\nExemplo de combinações de palavras:")
print(list(combinations(list(contagem.keys())[:6], 2)))

# -------------------------------------------------
# 3. Análise assíncrona com asyncio
# -------------------------------------------------
async def analisar_post(post):
    await asyncio.sleep(1)  # simula processamento pesado
    return f"Post {post['id']} analisado (user {post['userId']})"

async def pipeline():
    tarefas = [analisar_post(post) for post in resultados]
    for concluido in await asyncio.gather(*tarefas):
        print(concluido)

print("\n[INFO] Rodando análises assíncronas...")
asyncio.run(pipeline())
