import requests
import random
import time
import math
import json
from config import URL_API_IMOVEIS, HEADERS, PARAMETROS_BUSCA, TIMEOUT


def coletar_pagina(URL_API_IMOVEIS, parametros_busca, headers):
    """
Busca uma página de imóveis na API e organiza os dados.

Ela:
- chama a API
- pega os imóveis da resposta
- monta uma lista organizada com os dados de cada imóvel
- ignora erros de requisição ou dados quebrados

Args:
    parametros_busca (dict): dados usados na requisição
    headers (dict): cabeçalhos da requisição

Returns:
    list: lista de imóveis organizados (dicionários)
    Retorna None se não for possível obter os dados.
"""
    
    lista_imoveis = []
    
    try:
        
        resposta = requests.post(URL_API_IMOVEIS, data=parametros_busca, headers=headers, timeout=TIMEOUT)
        resposta.raise_for_status()
        dados_da_api = resposta.json()
        time.sleep(random.uniform(3.0,7.0))
        
    except (requests.exceptions.RequestException, json.JSONDecodeError) as err:
        print(f'[ERRO API] {err}')
        return None
           
    try:
        lista_imoveis_brutos = dados_da_api['lista']
    except KeyError as erru:
        print(f"[ERRO ESTRUTURA] chave faltando: {erru}")
        return None
        
    for imovel in lista_imoveis_brutos:
        
        try:
        
            codigo = imovel['codigo']
            
            data_hora_cadastro = imovel['datahoracadastro']
            
            codigo_finalidade = imovel['codigofinalidade']
            
            titulo_do_imovel = imovel['titulo']
            
            tipo_de_imovel = imovel['tipo']
            
            bairro_do_imovel = imovel['bairro']
            
            cidade = imovel['cidade']
            
            estado = imovel['estado']
            
            valor_do_imovel = imovel['valor']
            
            valor_numerico_imovel = imovel['valortratado']
            
            numero_de_quartos = imovel['numeroquartos']
            
            numero_de_banhos = imovel['numerobanhos']
            
            numero_de_vagas = imovel['numerovagas']
            
            numero_de_suites = imovel['numerosuites']
            
            area_interna = imovel['areainterna']
            
            latitude = imovel['latitude']
            
            longitude = imovel['longitude']
            
            link_imovel = 'https://www.ctiimobiliaria.com.br/imovel/' + imovel['url_amigavel'] + '/' + str(imovel['codigo'])
            
            registro_imovel = {
                'codigo' : codigo,
                'tipo_de_imovel' : tipo_de_imovel,
                'titulo_do_imovel' : titulo_do_imovel,
                'area_interna(m²)' : area_interna,
                'numero_de_quartos' : numero_de_quartos,
                'numero_de_suites' : numero_de_suites,
                'numero_de_banhos' : numero_de_banhos,
                'numero_de_vagas' : numero_de_vagas,
                'bairro_do_imovel' : bairro_do_imovel,
                'cidade' : cidade,
                'estado' : estado,
                'latitude' : latitude,
                'longitude' : longitude,
                'valor_do_imovel' : valor_do_imovel,
                'valor_numerico_imovel' : valor_numerico_imovel,
                'codigo_finalidade' : codigo_finalidade,
                'data_hora_cadastro' : data_hora_cadastro,
                'link_imovel' : link_imovel
            }
            
            lista_imoveis.append(registro_imovel)
            
        except KeyError as errito:
            print(f"[PULANDO IMÓVEL] campo faltando: {errito}")
            continue
        
    return lista_imoveis
   

def qtd_paginas():
    """
calcula quantas paginas tem no site

Ela:
- faz uma requisição para a API de imóveis
- lê o total de imóveis disponíveis
- usa a quantidade de imóveis por página para calcular quantas páginas existem

Args:
  Nenhum (usa parâmetros globais de configuração)

Returns:
    int: numero de paginas
    Retorna None se não for possível obter os dados.
"""
    
    try:
        
        resposta = requests.post(URL_API_IMOVEIS, data=PARAMETROS_BUSCA, headers=HEADERS, timeout=TIMEOUT)
        resposta.raise_for_status()
        dados_api = resposta.json()
        time.sleep(random.randint(3,7))
    except (requests.exceptions.RequestException, json.JSONDecodeError) as fail:
            print(f"[ERRO API] {fail}")
            return None
        
        
    try:
        imoveis = dados_api['lista']
    except KeyError as e:
        print(f"[ERRO ESTRUTURA] chave faltando: {e}")
        return None
    
    try:
        total_registros_numero = imoveis[0]['total_registros']
    except (IndexError, KeyError) as e:
        print(f"[ERRO PAGINAÇÃO] {e}")
        return None
    
    
    numero_registros = int(PARAMETROS_BUSCA['numeroregistros'])

    total_paginas = math.ceil(total_registros_numero / numero_registros)
        
    return total_paginas
   

def coletar_todos_os_imoveis():
    """
Busca todas as página de imóveis na API e retorna os dados em uma lista.

Ela:
- chama a outras funçoes de coleta
- orquestra o processo de paginaçao
- acumula os imoveis de múltiplas páginas em uma unica lista

Args:
    Nenhum (usa parâmetros globais de configuração)

Returns:
    list: lista de imóveis organizados (dicionários)
"""
    
    todos_os_imoveis = []

    total_paginas = qtd_paginas()
    
    for i in range(1, total_paginas + 1):
        print('-'*60)
        print(f'Buscando página {PARAMETROS_BUSCA['numeropagina']}/{total_paginas}...')
        imoveis_pagina = coletar_pagina(URL_API_IMOVEIS, PARAMETROS_BUSCA, HEADERS)
        
        if imoveis_pagina:
            print(f'Pagina {PARAMETROS_BUSCA['numeropagina']}: {len(imoveis_pagina)} imóveis coletados')
        
        if imoveis_pagina is not None:
            todos_os_imoveis.extend(imoveis_pagina)
        else:
            print('[ERRO] pagina retornou vazia')
        
        PARAMETROS_BUSCA['numeropagina'] = str(i+1)
        
    print('='*60)
    print('COLETA FINALIZADA')
    print('='*60)
    print(f'Total: {len(todos_os_imoveis)} imóveis coletados')
    print(f'Total de paginas: {total_paginas}')
        
    return todos_os_imoveis

