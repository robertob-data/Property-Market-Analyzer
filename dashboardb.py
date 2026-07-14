import matplotlib.pyplot as plt
import os


def criar_grafico(resumo):
    
    plt.figure(figsize=(16,10))
    
    #cabeçalho
    plt.suptitle(
    "PROPERTY MARKET ANALYZER",
    fontsize=18,
    fontweight="bold"
)
    
    total = resumo["total_de_imoveis"]

    media = resumo["preco_medio_imoveis"]

    maior = resumo["maior_preco_imoveis"]

    menor = resumo["menor_preco_imoveis"]
    
    plt.figtext(
    0.02,
    0.94,
    f"Total de imóveis: {total}"
    )
    
    plt.figtext(
    0.30,
    0.94,
    f"Preço médio: {media}"
    )
    
    plt.figtext(
    0.60,
    0.94,
    f"Maior preço: {maior}"
    )
    
    plt.figtext(
    0.82,
    0.94,
    f"Menor preço: {menor}"
    )
    
    #bloco1
    ranking = resumo['ranking_dos_bairros'].most_common(10)
    
    bairros = []
    qtd_bairros = []
    
    for bairro, quantidade in ranking:
        bairros.append(bairro)
        qtd_bairros.append(quantidade)
    
    
    plt.subplot(2,2,1)
    plt.barh(bairros, qtd_bairros)
    plt.grid(axis="x")
    for bairro, quantidade in zip(bairros, qtd_bairros):
        plt.text(quantidade, bairro, f" {quantidade}")
    plt.title(
    "Ranking Bairros",
    fontsize=12
    )
    
    #bloco2
    ranking = resumo['ranking_dos_tipos_imoveis'].most_common(10)
    
    tipos = []
    qtd_tipos = []
    
    for tipo, qtd_tipo in ranking:
        tipos.append(tipo)
        qtd_tipos.append(qtd_tipo)
    
    plt.subplot(2,2,2)
    plt.barh(tipos, qtd_tipos)
    plt.grid(axis="x")
    for tipo, qtd_tipo in zip(tipos, qtd_tipos):
        plt.text(qtd_tipo, tipo, f" {qtd_tipo}")
        
    plt.title(
    "Ranking Tipos De Imoveis",
    fontsize=12
)
    
    #bloco3
    ranking = resumo['ranking_das_cidades'].most_common(10)
    
    cidades = []
    qtd_cidades = []
    
    for cidade, qtd_cidade in ranking:
        cidades.append(cidade)
        qtd_cidades.append(qtd_cidade)
    
    plt.subplot(2,2,3)
    plt.barh(cidades, qtd_cidades)
    plt.grid(axis="x")
    for cidade, qtd_cidade in zip(cidades, qtd_cidades):
        plt.text(qtd_cidade, cidade, f" {qtd_cidade}")
    plt.title(
    "Ranking Cidades",
    fontsize=12
)
    
    #bloco4
    ranking = resumo['ranking_dos_quartos'].most_common(10)
    
    quartos = []
    qtd_quartos = []
    
    for quarto, qtd_quarto in ranking:
        quartos.append(quarto)
        qtd_quartos.append(qtd_quarto)
    
    plt.subplot(2,2,4)
    plt.barh(quartos, qtd_quartos)
    plt.grid(axis="x")
    for quarto, qtd_quarto in zip(quartos, qtd_quartos):
        plt.text(qtd_quarto, quarto, f" {qtd_quarto}")
    plt.title(
    "Quantidade De Quartos",
    fontsize=12
)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    os.makedirs("dashboard", exist_ok=True)
    plt.savefig("dashboard/dashboard.png")
    plt.close()