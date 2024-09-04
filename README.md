# Interpolação espacial
Aplicação do método IDW para interpolação espacial para preencher dados faltantes de precipitação nos meses Janeiro, Fevereiro e Março no Município de Rio Verde (GO)

## Portal HidroWeb 
O portal HidroWeb é um sistema que disponibiliza as informações coletadas pela Rede Hidrometeorológica Nacional (RHN), reunindo dados de volume de chuvas num determinado ponto, nível e vazão de rios, climatologia, qualidade da água e sedimentos (ANA, 2023).

Ao obter os dados de precipitação entre Janeiro e Março em diferentes estações hidrometeorológicas do Município de Rio Verde (GO) e em seus arredores, observou-se valores diversos valores faltantes, classificados com o número "-1" na tabela. 

## Inverse Distance Weight (IDW) - Interpolação espacial
A interpolação é uma técnica utilizada para estimativa do valor de uma variável em locais não amostrados a partir de dados pontuais existentes na mesma região. A ideia básica que envolve os processos de interpolação é que os valores da variável estudada tendem a ser mais similares aos de locais mais próximos que aos de locais mais distantes (SILVA, 2007).

O Inverse Distance Weight (IDW), é um dos métodos mais utilizados para interpolação espacial de variáveis ambientais (JÚNIOR et al., 2019). Seu pressuposto está no fato de que a estimativa de um ponto a ser medido sofre influência local de pontos próximos, que se reduz quando sua distância é maior (LI; HEAP, 2008). Desta maneira, o IDW define que o peso de cada valor é função do inverso de uma potência da distância, conforme exposto na equação abaixo.

![Interpolação espacial](https://github.com/user-attachments/assets/f6aa51f8-b246-47e9-a296-07c06dc4c694)

Onde:
- Vi​ é o valor desconhecido a ser estimado; 
- n é o número de pontos conhecidos utilizados para calcular o valor desconhecido;
- Vj é o valor conhecido no ponto j;
- dij é a distância entre o ponto 𝑖 (onde o valor é desconhecido) e o ponto 𝑗 (onde o valor é conhecido);
- 𝑝 é o expoente ou potência que controla a influência da distância na ponderação. Quanto maior o valor de p, menor será a influência de pontos mais distantes.

Passos (2019) e Silva (2013) apontam que o expoente p de valor 2 apresenta o melhor desempenho na espacialização dos valores de precipitação. Portanto, esse valor será utilizado.

## Estruturação de dados
Ao baixar os dados da soma de precipitação mensal do portal HidroWeb, certifique-se de gerar uma aba para cada estação, contendo as seguintes colunas: Ano, Mês 1, Mês 2,..., Latitude, Longitude. Por exemplo, no arquivo anexado os meses de estudo foram Janeiro, Fevereiro e Março, logo o DataFrame contém as colunas:
Ano | Janeiro | Fevereiro | Março | Latitude | Longitude

## Aplicação de substituição direta e IDW no seu script
Antes de aplicar o IDW, pode ser feita a substituição direta, isto é, quando houver uma estação com dados válidos para aquela(s) data(s) e todas as outras não.
No script de substituição direta, um novo arquivo .xlsx é gerado: 'df_substituicao_direta.xlsx'. 

Caso a substituição direta não tenha retirado todos os valores "-1", é feita a aplicação do IDW em cima do novo arquivo gerado. Nesse script a equação é aplicada em cada estação, e espera-se que não tenha sobrado mais nenhum valor faltante. Caso falte, isso significa que nenhuma estação possuía dados válidos naquela data em específico.

## Referências

AGÊNCIA NACIONAL DE ÁGUAS E SANEAMENTO BÁSICO (ANA). Hidroweb está disponível para usuários(as). Portal Governo do Brasil, 2023. Disponível em: https://www.gov.br/ana/pt-br/assuntos/noticias-e-eventos/noticias/hidroweb-esta-disponivel-para-usuarios-as. Acesso em: 20 ago. 2024.

JÚNIOR, J. C. da S. et al. Random forest techniques for spatial interpolation of evapotranspiration data from Brazilian’s northeast. Computers and Electronics in Agriculture, v. 166, p. 105017, 2019. ISSN 0168-1699. Disponível em: http://www.sciencedirect.com/science/article/pii/S0168169919302315. Acesso em: 19 ago. 2024.

LI, J.; HEAP, A. D. Areviewofspatial interpolation methods for environmental scientists. Canberra: Geoscience Australia, 2008. OCLC: 312275544. ISBN 978-1-921498-30-5 978-1-921498-28-2.

PASSOS, J. B. M. C.; LIMA, R. P. C.; DIAS, R. L. S. Análise do desempenho de diferentes potências para o interpolador IDW na bacia do rio Doce. In: XXIII Simpósio Brasileiro de Recursos Hídricos, 2019, Foz do Iguaçu - PR. Anais XXIII SBRH, 2019.

SILVA, Jackscilene Nascimento; DA SILVA CAIADO, Estela; CAIADO, Marco Aurélio Costa. Escolha de parâmetro para interpolação de precipitação diária utilizando o interpolador Inverse Distance Weight (IDW). In: XX Simpósio Brasileiro de Recursos Hídricos, 2013, Bento Gonçalves.

SILVA, K. R.; PAIVA, Y. G.; CECÍLIO, R. A.; PEZZOPANE, J. E. M. Avaliação de interpoladores para a espacialização de variáveis climáticas na bacia do rio Itapemirim-ES. In: Anais do 13º Simpósio Brasileiro de Sensoriamento Remoto, 2007, Florianópolis, NPE, 2007. p. 3141-3146.
