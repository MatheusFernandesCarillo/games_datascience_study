import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#export the database file
games = pd.read_csv("/content/Video_Games_Sales_as_at_22_Dec_2016.csv")

#Change the name of the columns to portuguese
games.columns = ["Nome", "Plataforma", "Lançamento", "Genero", "Publicadora", "Vendas_EUA", "Vendas_Europa", "Vendas_Japão", "Vendas_Outros", "Vendas_Global", "Nota_Critica", "Contagem_Criticos", "Nota_Usuario", "Contagem_Usuarios", "Desenvolvedora", "Classificação"]

#platform with more games
Jogos_por_plataforma = games["Plataforma"].value_counts()
print(Jogos_por_plataforma)
