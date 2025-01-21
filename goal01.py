import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#export the database file
games = pd.read_csv("/content/Video_Games_Sales_as_at_22_Dec_2016.csv")

#Change the name of the columns to portuguese
games.columns = ["Nome", "Plataforma", "Lançamento", "Genero", "Publicadora", "Vendas_EUA", "Vendas_Europa", "Vendas_Japão", "Vendas_Outros", "Vendas_Global", "Nota_Critica", "Contagem_Criticos", "Nota_Usuario", "Contagem_Usuarios", "Desenvolvedora", "Classificação"]

#create a variable just for Pokémon games
pokemon_games = games[games["Nome"].str.contains("pokemon", case=False, na=False)]

#create a variable with the Pókemon games sorted by global sales
pokemon_games_ordenado = pokemon_games.sort_values(by="Vendas_Global", ascending=False)

#creating a new column to show the plataform for the hue
pokemon_games_ordenado["Plataforma"] = pokemon_games_ordenado["Plataforma"].astype(str)

plt.figure(figsize=(16, 8))
sns.barplot(
    x="Nome",
    y="Vendas_Global",
    hue="Plataforma", 
    data=pokemon_games_ordenado,
    dodge=False 
)

#adjusting the chart to make it easier to understand
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.xlabel("Nome do Jogo", fontsize=14)
plt.ylabel("Vendas Globais (em milhões)", fontsize=14)
plt.title("Vendas Globais de Jogos Pokémon até 2016", fontsize=16, weight='bold')
plt.legend(title="Plataforma", fontsize=12, title_fontsize=14)
plt.tight_layout()
plt.show()
