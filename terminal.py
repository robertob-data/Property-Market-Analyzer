def mostrar_cabecalho():
    print("=" * 60)
    print("                 Property Market Analyzer")
    print("=" * 60)


def mostrar_resumo(resumo):
    print("\nRESUMO GERAL")
    print("-" * 60)
    print(f"Total de imóveis : {resumo['total_de_imoveis']}")
    print(f"Preço médio      : {resumo['preco_medio_imoveis']}")
    print(f"Maior preço      : {resumo['maior_preco_imoveis']}")
    print(f"Menor preço      : {resumo['menor_preco_imoveis']}")


def mostrar_ranking(titulo, ranking, limite=5):
    print(f"\n{titulo}")
    print("-" * 60)

    for posicao, (nome, quantidade) in enumerate(ranking.most_common(limite), start=1):
        print(f"{posicao:>2}º {nome:<30} {quantidade}")


def mostrar_media_bairros(media_bairros):
    print("\nMÉDIA DE PREÇO POR BAIRRO")
    print("-" * 60)

    for bairro, media in media_bairros.items():
        print(f"{bairro:<30} {media}")


def mostrar_finalizacao():
    print("\n" + "=" * 60)
    print("Processo finalizado com sucesso!")
    print("=" * 60)
    input("\nPressione ENTER para sair...")


def exibir_resumo_terminal(resumo):
    mostrar_resumo(resumo)

    mostrar_ranking(
        "TOP BAIRROS",
        resumo["ranking_dos_bairros"]
    )

    mostrar_ranking(
        "TOP CIDADES",
        resumo["ranking_das_cidades"]
    )

    mostrar_ranking(
        "TIPOS DE IMÓVEIS",
        resumo["ranking_dos_tipos_imoveis"]
    )

    mostrar_ranking(
        "QUANTIDADE DE QUARTOS",
        resumo["ranking_dos_quartos"]
    )

    mostrar_media_bairros(
        resumo["media_por_bairro"]
    )