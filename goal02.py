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

print(pokemon_games_ordenado[["Nome", "Vendas_Global"]])
