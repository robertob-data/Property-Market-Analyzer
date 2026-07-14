import time
from scraper import coletar_todos_os_imoveis
from analyzer import resumo_geral
from exporter import exportar_excel, exportar_csv, exportar_json, resumo_json
from terminal import exibir_resumo_terminal, mostrar_finalizacao
from dashboardb import criar_grafico


print('\n=== Property Market Analyzer ===')
time.sleep(0.3)
print('Iniciando coleta...')
time.sleep(0.3)

imoveis_coletados = coletar_todos_os_imoveis()

if imoveis_coletados:
    
    print('='*60)
    print('Iniciando Analise Dos Imoveis...')
    time.sleep(0.5)

    if imoveis_coletados:
        print('Analise Concluida!')
        resumo = resumo_geral(imoveis_coletados)
        exibir_resumo_terminal(resumo)
        criar_grafico(resumo)
    else:
        print('Nenhum Imovel Encontrado Para Analise')
        
    print('-'*60)
    print('Iniciando Exportaçao Para Excel')
    time.sleep(0.3)
    if imoveis_coletados:
        exportar_excel(imoveis_coletados)
        print('Excel Gerado Com Sucesso')
    print('-'*60)

    print('Iniciando Exportaçao Para CSV')
    time.sleep(0.3)
    if imoveis_coletados:
        exportar_csv(imoveis_coletados)
        print('CSV Gerado Com Sucesso')
    print('-'*60)

    print('Iniciando Exportaçao Para Json')
    time.sleep(0.3)
    if imoveis_coletados:
        exportar_json(imoveis_coletados)
        print('Json Gerado Com Sucesso')
    print('-'*60)
    
else:
    print('Nenhum Imóvel Encontrado Para Análise ou Exportação.')
    print('=' * 60)

mostrar_finalizacao()