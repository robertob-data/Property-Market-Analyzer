URL_API_IMOVEIS = 'https://www.ctiimobiliaria.com.br/retornar-imoveis-disponiveis'
    
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/15'
    }

PARAMETROS_BUSCA = {"finalidade":"aluguel",
    "codigounidade" : "",
    "codigocondominio" : "0",
    "codigoproprietario" : "0",
    "codigocaptador" : "0",
    "codigosimovei" : "0",
    "codigocidade" : "0",
    "codigoregiao" : "0",
    "bairros[0][cidade]" : "",
    "bairros[0][codigo]" : "",
    "bairros[0][estado]" : "",
    "bairros[0][estadoUrl]" : "",
    "bairros[0][nome]" : "Todos",
    "bairros[0][nomeUrl]" : "todos-os-bairros",
    "bairros[0][regiao]" : "",
    "endereco" : "",
    "edifici" : "",
    "numeroquartos" : "0",
    "numerovagas" : "0",
    "numerobanhos" : "0",
    "numerosuite" : "0",
    "numerovaranda" : "0",
    "numeroelevador" : "0",
    "valorde" : "0",
    "valorate" : "0",
    "areade" : "0",
    "areaate" : "0",
    "areaexternade" : "0",
    "areaexternaate" : "0",
    "destaque" : "1",
    "opcaoimovel[codigo]" : "0",
    "opcaoimovel[nome]" : "",
    "opcaoimovel[nomeUrl]" : "todas-as-opcoes",
    "codigoOpcaoimovel" : "0",
    "retornomapaapp" : "false",
    "numeropagina" : "1", #paginaçao aqui
    "numeroregistros" : "20",
    "ordenacao" : "dataatualizacaodesc",
    "codigoempreendimentomae" : "",
    "condominio[codigo]" : "0",
    "condominio[nome]" : "",
    "condominio[nomeUrl]" : "todos-os-condominios"
    }
    
TIMEOUT = 10