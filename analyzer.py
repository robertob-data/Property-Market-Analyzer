from collections import Counter
from collections import defaultdict

def total_imoveis(lista_imoveis):
    """
    Calcula a quantidade total de imóveis.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        int: quantidade total de imóveis.
    """

    return len(lista_imoveis)

def preco_medio(lista_imoveis):
    """
    Calcula o preço medio dos imóveis.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        float: preço medio dos imóveis.
    """
    
    soma = 0
    
    if not lista_imoveis:
        return None
    
    for imovel in lista_imoveis:
        soma += imovel['valor_numerico_imovel']
        
    medio = soma / len(lista_imoveis)
    return medio

def maior_preco(lista_imoveis):
    """
    Retorna o maior valor de aluguel encontrado.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        float : maior valor encontrado.
    """
    if not lista_imoveis:
        return None
    
    return max(imovel['valor_numerico_imovel'] for imovel in lista_imoveis)

def menor_preco(lista_imoveis):
    """
    Retorna o menor valor de aluguel encontrado.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        float : menor valor encontrado.
    """
    if not lista_imoveis:
        return None
    
    return min(imovel['valor_numerico_imovel'] for imovel in lista_imoveis)

def ranking_bairros(lista_imoveis):
    """
    Retorna um ranking dos bairros.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        dict | dict: ranking dos bairros.
    """
    
    if not lista_imoveis:
        return None
    
    bairros = []
    
    for imovel in lista_imoveis:
        bairro = imovel['bairro_do_imovel']
        bairros.append(bairro)
    
    return Counter(bairros)

def ranking_cidades(lista_imoveis):
    """
    Retorna um ranking das cidaddes.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        dict | dict: ranking das cidades.
    """
    
    if not lista_imoveis:
        return None
    
    cidades = []
    
    for imovel in lista_imoveis:
        cidade = imovel['cidade']
        cidades.append(cidade)
        
    return Counter(cidades)

def ranking_tipos(lista_imoveis):
    """
    Retorna um ranking dos tipos de imoveis.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        dict | dict: ranking dos tipos de imoveis.
    """
    
    if not lista_imoveis:
        return None
    
    tipos_imoveis = []
    
    for imovel in lista_imoveis:
        tipo_imovel = imovel['tipo_de_imovel']
        tipos_imoveis.append(tipo_imovel)
        
    return Counter(tipos_imoveis)

def ranking_quartos(lista_imoveis):
    """
    Retorna um ranking da quantidade de quartos.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        dict | dict: ranking da quantidade dos quartos.
    """
    
    if not lista_imoveis:
        return None
    
    quartos = []
    
    for imovel in lista_imoveis:
        quarto = imovel['numero_de_quartos']
        quartos.append(quarto)
        
    return Counter(quartos)

def media_bairro(lista_imoveis):
    """
    Retorna a média de preço dos imóveis por bairro.

    Args:
        lista_imoveis (list): lista contendo os imóveis coletados.

    Returns:
        dict: média de preço por bairro.
    """

    if not lista_imoveis:
        return None

    imoveis_por_bairro = defaultdict(list)

    # Agrupa os preços por bairro
    for imovel in lista_imoveis:
        bairro = imovel['bairro_do_imovel']
        preco = imovel['valor_numerico_imovel']

        imoveis_por_bairro[bairro].append(preco)

    medias = {}

    # Calcula a média de cada bairro
    for bairro, precos in imoveis_por_bairro.items():
        medias[bairro] = sum(precos) / len(precos)

    return medias

def resumo_geral(lista):
    
    total_de_imoveis = total_imoveis(lista)
    
    preco_medio_imoveis = preco_medio(lista)
    
    maior_preco_imoveis = maior_preco(lista)
    
    menor_preco_imoveis = menor_preco(lista)
    
    ranking_dos_bairros = ranking_bairros(lista)
    
    ranking_das_cidades = ranking_cidades(lista)
    
    ranking_tipos_imoveis = ranking_tipos(lista)
    
    ranking_dos_quartos = ranking_quartos(lista)
    
    media_por_bairro = media_bairro(lista)
    
    media_por_bairro_formatada = {
        bairro: f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        for bairro, valor in media_por_bairro.items()
    } if media_por_bairro else None

    registro_analyzer = {
        'total_de_imoveis' : total_de_imoveis,
        # Formata os preços individuais diretamente aqui usando f-strings
        'preco_medio_imoveis' : f"R$ {preco_medio_imoveis:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if preco_medio_imoveis else "R$ 0,00",
        'maior_preco_imoveis' : f"R$ {maior_preco_imoveis:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if maior_preco_imoveis else "R$ 0,00",
        'menor_preco_imoveis' : f"R$ {menor_preco_imoveis:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if menor_preco_imoveis else "R$ 0,00",
        'ranking_dos_bairros' : ranking_dos_bairros,
        'ranking_das_cidades' : ranking_das_cidades,
        'ranking_dos_tipos_imoveis' : ranking_tipos_imoveis,
        'ranking_dos_quartos' : ranking_dos_quartos,
        'media_por_bairro' : media_por_bairro_formatada
    }
    
    
    return registro_analyzer


