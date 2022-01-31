from fpdf import FPDF
import pandas as pd
import os
import matplotlib.pyplot as plt

pdf = FPDF('p', 'mm', 'A4')
pdf.add_page()
pdf.set_font('times', '', 20)

dadosEstado = pd.read_excel(r'Dados-covid-19-estado.xlsx')
dados_municipios = pd.read_excel(r'Dados-covid-19-municipios.xlsx')

casos_muni = dados_municipios["Mun_Total de casos"]
obito_muni = dados_municipios["Mun_Total de óbitos"]
muni = dados_municipios["Município"]

total_casos = dadosEstado["Total de casos"]
casos_dia = dadosEstado["Casos por dia"]
obitos_dia = dadosEstado["Óbitos por dia"]

municipios_maiores_casos = []
municipios_maiores_obitos = []
maior_caso = 0
maior_obito = 0
indice_maior_caso = 0
indice_maior_obito = 0
texto_muni = "\n\n"

for x in range (len(list(casos_muni))):
    try:
        if int(list(casos_muni)[x])>maior_caso:
            maior_caso=int(list(casos_muni)[x])
            indice_maior_caso=x
    except:
        print("Erro: leitura de casos.")

    try:
        if int(list(obito_muni)[x])>maior_obito:
            maior_obito=int(list(obito_muni)[x])
            indice_maior_obito=x
    except:
        print("Erro: leitura de óbitos.")

for z in range (len(list(muni))):
    try:
        if int(list(casos_muni)[z])==maior_caso:
            municipios_maiores_casos.append(list(muni)[z])
    except:
        print("Erro de leitura.")

    try:
        if int(list(obito_muni)[z])==maior_obito:
            municipios_maiores_obitos.append(list(muni)[z])
    except:
        print("Erro de leitura.")

texto_muni+="Municípios que tiveram maiores casos("+str(maior_caso)+"): "

for y in range (len(municipios_maiores_casos)):
    if (y+1)!=len(municipios_maiores_casos):
        texto_muni+=municipios_maiores_casos[y]+", "
    else:
        texto_muni+=municipios_maiores_casos[y]
    texto_muni+="\n\n"

texto_muni+="Municípios que tiveram maiores óbitos("+str(maior_obito)+"): "

for m in range (len(municipios_maiores_obitos)):
    if (m+1)!=len(municipios_maiores_obitos):
        texto_muni+=municipios_maiores_obitos[m]+", "
    else:
        texto_muni+=municipios_maiores_obitos[m]
    texto_muni+="\n\n"

texto_relatorio_covid = "COVID-19 e o desemprego no Brasil.\n\n""	A COVID-19 teve grande impacto em diferentes espaços da sociedade, por exemplo; nas relações interpessoal, na saúde, na econômia, na mídia, mercado de trabalho. E de acordo com os dados, esses problemas só tendem a piorar com o passar dos anos. Ainda que todo o Mundo tenha problemas financeiros e sociais, o Brasil está em colapso.\n\n	Em 2019, o Brasil registrou 12,5 milhões de desempregados no último trimestre. No ano seguinte, com o início da pandemia, o número de pessoas nessa condição subiu para 13,2 milhões. Os dados divulgados pelo Instituto Brasileiro de Geografia e Estatística (IBGE) mostraram que a taxa de desemprego chegou a 13,9% nos últimos três meses de 2020. O primeiro trimestre de 2020 terminou com a maior taxa de desemprego e o maior contingente de pessoas sem trabalho na série histórica, em meio aos desafios impostos pela piora da pandemia de Covid-19 no Brasil. Em 2022 terá 14 milhões de desempregados, de acordo com a projeção divulgada pela Organização Internacional do Trabalho (OTI). A perspectiva é de que o país retorne ao índice de desemprego de antes da pandemia apenas em 2023 ou 2024 (para 2023, taxa de desemprego deve cair para 13,6 milhões de pessoas).\n\n	A Organização Internacional do Trabalho (OTI) também alertou sobre o impacto global da pandemia no emprego e prevê recuperação lenta e incerta do mercado de trabalho.\n\nFontes:\n\nhttps://www.poder360.com.br/economia/brasil-tera-14-milhoes-de-desempregados-em-2022-diz-oit/\n\nhttps://www.poder360.com.br/economia/brasil-tera-14-milhoes-de-desempregados-em-2022-diz-oit/#:~:text=O%20Brasil%20ter%C3%A1%2014%20milh%C3%B5es,apenas%20em%202023%20ou%202024.\n\nhttps://dcomercio.com.br/categoria/economia/impactos-economicos-da-pandemia-no-brasil-estao-entre-os-mais-graves\n\n \n\n Municípios de maiores casos:"+texto_muni

plt.plot(total_casos)
plt.xlabel('Total de casos')
plt.savefig("grafico_1.png")
plt.close()

pdf.multi_cell(w=0, h=8, txt="Gráfico de casos no estado de SP", ln=1, align='C')

pdf.image(x=20, y=30, w=180, h=80, name='grafico_1.png')

plt.plot(casos_dia)
plt.xlabel('Casos por dia')
plt.savefig("grafico_2.png")
plt.close()

pdf.multi_cell(w=0, h=230, txt="Casos diários no estado de SP", ln=1, align='C')
pdf.image(x=20, y=140, w=180, h=80, name='grafico_2.png')

plt.plot(obitos_dia)
plt.xlabel('Obitos por dia')
plt.savefig("grafico_3.png")
plt.close()

pdf.multi_cell(w=0, h=30, txt="Óbitos diários no Estado de SP", ln=1, align='C')
pdf.image(x=20, y=50, w=180, h=80, name='grafico_3.png')
pdf.add_page()

pdf.multi_cell(w=0, h=8, txt=texto_relatorio_covid, ln=1, align='C')

pdf.output('Relatório.pdf')

os.system("pause")