import pandas as pd
import numpy as np

# seeds lê o arquivo csv 
seeds = pd.read_csv('https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv', header=None, index_col=None)

# tabela recebe a tabela csv 
tabela = pd.DataFrame(seeds)

# Remove as colunas extras no final 
tabela.drop(columns = [6, 7, 8], axis = 1, inplace=True)

# Adiciona linha de cabeçalho 
tabela.columns = ["Área A", "Perímetro P", "Extensão do núcleo", "Largura", "Coeficiente de Assimetria", "Extensão do sulgo do núcleo"]

# Remove as linha com valores nulos
tabela.dropna(axis=0, how="any", inplace=True)

#Adicionar um campo Compactação com o cálculo é C = 4*pi*A/P^2
tabela["Campo compactação"] = 4 * np.pi * (tabela["Área A"]) / (tabela["Perímetro P"]**2)

print(tabela)

# Exportar para CSV o valor final
tabela.to_csv("tratamentos-de-dados.csv")

