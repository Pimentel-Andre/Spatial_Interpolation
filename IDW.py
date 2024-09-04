import pandas as pd
import numpy as np
from scipy.spatial import cKDTree  
# A interpolação irá usar a estrutura cKDTree para encontrar os vizinhos mais próximos de cada ponto desconhecido, ou seja, os que têm valores a serem interpolados


# Geração de lista com os nomes das estações que serão o nome de cada aba nas planilhas
a = 'estacao_1'
b = 'estacao_2'
c = 'estacao_3'

sheet_names = [a, b, c]

# Caminho do arquivo gerado a partir do script de substituição direta
file_path = '/caminho/df_substituicao_direta.xlsx'

# Geração de uma lista contendo os caminhos para cada aba da planilha
dfs = [pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names]

def idw_interpolation(x, y, z, xi, yi, power=2): # O valor de potência pode ser alterado. Entretando, a literatura indica utilizar o valor 2 para esse caso
    tree = cKDTree(np.c_[x, y])
    d, idx = tree.query(np.c_[xi, yi], k=len(z))
    weights = 1 / d**power
    weights /= weights.sum(axis=1)[:, None]
    zi = np.sum(weights * z[idx], axis=1)
    return zi

def interpolate_spatial(df_combined, column): # Aqui, a função vai percorrer os anos únicos no df_combined e, para cada ano, separa os dados conhecidos (com valores válidos) e os "-1" (valores a serem interpolados)
    for year in df_combined['Data'].unique():
        known_data = df_combined[(df_combined['Data'] == year) & (df_combined[column] != -1)]
        unknown_data = df_combined[(df_combined['Data'] == year) & (df_combined[column] == -1)]

        if known_data.empty or unknown_data.empty:
            continue  # Se estiver vazio, não há nada a interpolar
          
        # abaixo são armazenados os valores conhecidos 
        x_known = known_data['Longitude'].values #valores de longitude das observações conhecidas (dados válidos)
        y_known = known_data['Latitude'].values #valores de latitude das observações conhecidas (dados válidos)
        z_known = known_data[column].values # extrai os valores de precipitação para o mês onde eles estão disponíveis.

        '''Essas três variáveis são usadas juntas na interpolação espacial para estimar os valores de z, 
        onde tenho as coordenadas (x_unknown e y_unknown), mas não tenho dado válido z ''' 
      
        # aqui são armazenados os desconhecidos
        x_unknown = unknown_data['Longitude'].values
        y_unknown = unknown_data['Latitude'].values
      
        interpolated_values = idw_interpolation(x_known, y_known, z_known, x_unknown, y_unknown)

        df_combined.loc[(df_combined['Data'] == year) & (df_combined[column] == -1), column] = interpolated_values

    return df_combined

# Aqui, uno todos os DataFrames, ou seja, todas os dados das estações
df_combined = pd.concat(dfs, ignore_index=True)

# Aplico interpolação espacial para cada mês. Nas variáveis abaixo, você pode inserir o nome do meses de estudo. 
month1 = 'Jan'
month2 = 'Fev'
mont3 = 'Mar'

for month in ['Jan', 'Fev', 'Mar']:
    df_combined = interpolate_spatial(df_combined, month)

# Salvar o DataFrame processado, se necessário
df_combined.to_excel('df_interpolated_precipitacao_mensal.xlsx', index=False)

# Exibir os primeiros registros do DataFrame final para verificação
print(df_combined.head())
