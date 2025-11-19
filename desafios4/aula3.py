import requests
from bs4 import BeautifulSoup
import pandas as pd

# Faz scraping do G1
url = "https://www.lance.com.br/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extrai os títulos das notícias
titulos = soup.find_all("a", class_="feed-post-link")

# Organiza em DataFrame
dados = {
    "Título": [t.text.strip() for t in titulos[:10]]
}
df = pd.DataFrame(dados)

# Salva em CSV
df.to_csv("noticias_lance.csv", index=False)
print("🗂️ Arquivo CSV criado com sucesso!")
