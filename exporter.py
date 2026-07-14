import pandas as pd
import json
import os
from datetime import datetime

agora = datetime.now()
data_hora_arquivo = agora.strftime("%d-%m-%Y_%H-%M-%S")

os.makedirs("exports", exist_ok=True)

def exportar_excel(lista):
    df = pd.DataFrame(lista)
    df.to_excel(f'exports/imoveis_{data_hora_arquivo}.xlsx', index=False)

def exportar_csv(lista):
    df = pd.DataFrame(lista)
    df.to_csv(f'exports/imoveis_{data_hora_arquivo}.csv', index=False)

def exportar_json(lista):
    with open(f'exports/imoveis_{data_hora_arquivo}.json', 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)
    
def resumo_json(resumo):
    # Salva o dicionário único diretamente com formatação limpa
    with open('exports/resumo.json', 'w', encoding='utf-8') as f:
        json.dump(resumo, f, indent=4, ensure_ascii=False)
    

