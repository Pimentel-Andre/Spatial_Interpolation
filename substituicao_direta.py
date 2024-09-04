import pandas as pd

# Geração de lista com os nomes das estações que serão o nome de cada aba nas planilhas
a = 'estacao_1'
b = 'estacao_2'
c = 'estacao_3'

sheet_names = [a, b, c]

# Caminho do arquivo
file_path = '/caminho/Precipitacao_Rio_Verde.xlsx'

# Geração de uma lista contendo os caminhos para cada aba da planilha
dfs = [pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names]

def substituicao_direta_condicional(dfs):
    for year in dfs[0]['Data'].unique():
        for month in ['Jan', 'Fev', 'Mar']:
            values = [df.loc[df['Data'] == year, month].values[0] for df in dfs]
            if sum(v != -1 for v in values) == 1:
                valid_value = next(v for v in values if v != -1)
                for df in dfs:
                    df.loc[(df['Data'] == year) & (df[month] == -1), month] = valid_value
    return dfs

# Execução da Substituição Direta Condicional
dfs = substituicao_direta_condicional(dfs)

# Gero um novo arquivo Excel contendo as estações com os dados substituídos por substituição direta
with pd.ExcelWriter('df_substituicao_direta.xlsx') as writer:
    for i, df in enumerate(dfs):
        df.to_excel(writer, sheet_name=sheet_names[i], index=False)
