from unicodedata import normalize

import os


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


with open('nomes.txt', mode='w') as f:
    for nome in os.listdir('./cartas'):
        novo_nome = remover_acentos(nome)
        os.rename(f"./cartas/{nome}", f"./cartas/{novo_nome}")
        f.write(f'{novo_nome}\n')
